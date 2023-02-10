
def url_gen_nexrad(input):
    arr = input.split("_")[0]
    year, day, hour, station = arr[4:8], arr[8:10], arr[10:12], arr[0:4]
    fs = "https://noaa-nexrad-level2.s3.amazonaws.com/{}/{}/{}/{}/{}".format(year,day,hour,station,input)
    return fs

# Team 01
EXACT_URL_T1 = "https://noaa-nexrad-level2.s3.amazonaws.com/2011/06/12/KBGM/KBGM20110612_003045_V03.gz"
test = "KBGM20110612_003045_V03.gz"
test_fs_T1 = url_gen_nexrad(test)
assert(test_fs_T1 == EXACT_URL_T1)

# Team 02
EXACT_URL_T2 = "https://noaa-nexrad-level2.s3.amazonaws.com/2010/05/12/KARX/KARX20100512_014240_V03.gz"
test = "KARX20100512_014240_V03.gz"
test_fs_T2 = url_gen_nexrad(test)
assert(test_fs_T2 == EXACT_URL_T2)

# Team 03
EXACT_URL_T3 = "https://noaa-nexrad-level2.s3.amazonaws.com/2013/09/02/KABX/KABX20130902_002911_V06.gz"
test = "KABX20130902_002911_V06.gz"
test_fs_T3 = url_gen_nexrad(test)
assert(test_fs_T3 == EXACT_URL_T3)

# Team 04
EXACT_URL_T4 = "https://noaa-nexrad-level2.s3.amazonaws.com/2000/12/22/KBIS/KBIS20001222_090728.gz"
test = "KBIS20001222_090728.gz"
test_fs_T4 = url_gen_nexrad(test)
assert(test_fs_T4 == EXACT_URL_T4)

# Team 05
EXACT_URL_T5 = "https://noaa-nexrad-level2.s3.amazonaws.com/2012/02/03/KCCX/KCCX20120203_013605_V03.gz"
test = "KCCX20120203_013605_V03.gz"
test_fs_T5 = url_gen_nexrad(test)
assert(test_fs_T5 == EXACT_URL_T5)

# # Team 06
# EXACT_URL_T6 = ""
# test = "KCBW20011213_002358.gz"
# test_fs_T6 = url_gen_nexrad(test)
# assert(test_fs_T6 == EXACT_URL_T6)

# Team 07
EXACT_URL_T7 = "https://noaa-nexrad-level2.s3.amazonaws.com/2015/08/04/KBYX/KBYX20150804_000940_V06.gz"
test = "KBYX20150804_000940_V06.gz"
test_fs_T7 = url_gen_nexrad(test)
assert(test_fs_T7 == EXACT_URL_T7)

# Team 08
EXACT_URL_T8 = "https://noaa-nexrad-level2.s3.amazonaws.com/2012/07/17/KAPX/KAPX20120717_013219_V06.gz"
test = "KAPX20120717_013219_V06.gz"
test_fs_T8 = url_gen_nexrad(test)
assert(test_fs_T8 == EXACT_URL_T8)

# Team 09
EXACT_URL_T9 = "https://noaa-nexrad-level2.s3.amazonaws.com/2014/09/07/KAPX/KAPX20140907_010223_V06.gz"
test = "KAPX20140907_010223_V06.gz"
test_fs_T9 = url_gen_nexrad(test)
assert(test_fs_T9 == EXACT_URL_T9)

# Team 10
EXACT_URL_T10 = "https://noaa-nexrad-level2.s3.amazonaws.com/2008/08/19/KCBW/KCBW20080819_012424_V03.gz"
test = "KCBW20080819_012424_V03.gz"
test_fs_T10 = url_gen_nexrad(test)
assert(test_fs_T10 == EXACT_URL_T10)

# Team 11
EXACT_URL_T11 = "https://noaa-nexrad-level2.s3.amazonaws.com/1993/11/12/KLWX/KLWX19931112_005128.gz"
test = "KLWX19931112_005128.gz"
test_fs_T11 = url_gen_nexrad(test)
assert(test_fs_T11 == EXACT_URL_T11)

# Team 12
EXACT_URL_T12 = "https://noaa-nexrad-level2.s3.amazonaws.com/2003/07/17/KBOX/KBOX20030717_014732.gz"
test = "KBOX20030717_014732.gz"
test_fs_T12 = url_gen_nexrad(test)
assert(test_fs_T12 == EXACT_URL_T12)