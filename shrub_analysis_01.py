#!/usr/bin/env python3

import sys
import pandas

def analyseFile(fname):
    print(fname)
    print('------------------------')

    # parse CSV file
    types = {'Time': float, 'Type': str, 'SOM': str, 'Type/SEQ': str, 'length': str, 'data': str, 'LRC': str}
    df = pandas.read_csv(fname, index_col='Time', dtype=types, keep_default_na=False)

    # reports
    reportNumberOfPacketsByType(df)
    reportPacketRetransmissions(df)
    reportPacketFailures(df)

def reportNumberOfPacketsByType(df):
    # count the packets
    typeDict = {}
    for index, row in df.iterrows():
        if row['Type'] in typeDict:
            typeDict[row['Type']] += 1
        else:
            typeDict[row['Type']] = 1

    # print the report
    total = 0
    fmt = '{:30}{}'
    print('')
    print(fmt.format('Packet Type', 'Number Logged'))
    for item in typeDict.items():
        print(fmt.format(item[0], item[1]))
        total += item[1]
    print(fmt.format('Total', total))
    print('')

def reportPacketRetransmissions(df):
    print('')
    lastTypeSeqIn = ''
    lastTypeSeqOut = ''
    for index, row in df.iterrows():
        cmd = row['Type']
        if 'ACK' not in cmd:
            typeseq = row['Type/SEQ']
            if '<=' in cmd:
                if typeseq == lastTypeSeqIn:
                    print('Repeat "{}" (Type/SEQ {}) at {})'.format(cmd, typeseq, index))
                lastTypeSeqIn = typeseq
            elif '=>' in cmd:
                if typeseq == lastTypeSeqOut:
                    print('Repeat "{}" (Type/SEQ {}) at {})'.format(cmd, typeseq, index))
                lastTypeSeqOut = typeseq
    print('')

def reportPacketFailures(df):
    print('')
    foundNak = False
    for index, row in df.iterrows():
        if 'NAK' in row['Type']:
            print('{} at {}'.format(row['Type'], index))
            foundNak = True
    if not foundNak:
        print('No NAKs found')
    print('')

if len(sys.argv) < 2:
    raise Exception('No files specified!')

for fname in sys.argv[1:]:
    analyseFile(fname)
