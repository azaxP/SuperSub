
ENC = 'utf_8_sig'

with open(r'F:\Greys\Subs-5\Greys.Anatomy.S05E04.BRRip.x264-ION10.srt',
          mode='rb') as f:
    rBOM = f.read()



with open(r'F:\Greys\Greys.Anatomy.S06E04.WEBRip.x264-ION10.srt',
          mode='rb') as f:
    rUTF = f.read()
    pass



print("")

with open(r'S:\Desktop\test_srt.srt', 'wb') as wf:
    with open(r'F:\Greys\Greys.Anatomy.S06E04.WEBRip.x264-ION10.srt',
              mode='r') as rf:
        wf.write(rf.read().replace('\n', '\r\n').encode(ENC))

print("")