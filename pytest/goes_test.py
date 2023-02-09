

def url_gen_goes(input):
    arr = input.split("_")
    tproduct_code = arr[1].split("-")
    s1 = tproduct_code[2]
    finalProductCode =tproduct_code[0]+"-"+tproduct_code[1]+"-"+ ''.join([i for i in s1 if not i.isdigit()])
    date = arr[3]
    year, day_of_year, hour = date[1:5], date[5:8], date[8:10]
    fs = "https://noaa-goes18.s3.amazonaws.com/{}/{}/{}/{}/{}".format(finalProductCode,year,day_of_year,hour,input)
    print(fs)
    return fs

def test_url_gen1():
 # Team 01
 EXCEL_URL_T1 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-ACMM/2023/009/05/OR_ABI-L2-ACMM1-M6_G18_s20230090504262_e20230090504319_c20230090505026.nc"
 test = "OR_ABI-L2-ACMM1-M6_G18_s20230090504262_e20230090504319_c20230090505026.nc"
 test_fs_T1 = url_gen_goes(test)
 assert(test_fs_T1 == EXCEL_URL_T1)

def test_url_gen2():
 # Team 02
 EXCEL_URL_T2 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-ACTPM/2023/009/04/OR_ABI-L2-ACTPM1-M6_G18_s20230090408262_e20230090408319_c20230090409174.nc"
 test = "OR_ABI-L2-ACTPM1-M6_G18_s20230090408262_e20230090408319_c20230090409174.nc"
 test_fs_T2 = url_gen_goes(test)
 assert(test_fs_T2 == EXCEL_URL_T2)

def test_url_gen3():
 # Team  03
 EXCEL_URL_T3 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-DSIM/2023/011/06/OR_ABI-L2-DSIM1-M6_G18_s20230110608251_e20230110608308_c20230110609126.nc"
 test = "OR_ABI-L2-DSIM1-M6_G18_s20230110608251_e20230110608308_c20230110609126.nc"
 test_fs_T3 = url_gen_goes(test)
 assert(test_fs_T3 == EXCEL_URL_T3)

def test_url_gen4():
 # Team 04
 EXCEL_URL_T4 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-ACHTM/2022/356/08/OR_ABI-L2-ACHTM1-M6_G18_s20223560805242_e20223560805300_c20223560806526.nc"
 test = "OR_ABI-L2-ACHTM1-M6_G18_s20223560805242_e20223560805300_c20223560806526.nc"
 test_fs_T4 = url_gen_goes(test)
 assert(test_fs_T4 == EXCEL_URL_T4)

def test_url_gen5():
 # Team 05
 EXCEL_URL_T5 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-BRFF/2022/315/02/OR_ABI-L2-BRFF-M6_G18_s20223150230207_e20223150239515_c20223150241087.nc"
 test = "OR_ABI-L2-BRFF-M6_G18_s20223150230207_e20223150239515_c20223150241087.nc"
 test_fs_T5 = url_gen_goes(test)
 assert(test_fs_T5 == EXCEL_URL_T5)

def test_url_gen6():
 # Team 06
 EXCEL_URL_T6 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-ADPM/2023/006/13/OR_ABI-L2-ADPM2-M6_G18_s20230061310557_e20230061311015_c20230061311402.nc"
 test = "OR_ABI-L2-ADPM2-M6_G18_s20230061310557_e20230061311015_c20230061311402.nc"
 test_fs_T6 = url_gen_goes(test)
 assert(test_fs_T6 == EXCEL_URL_T6)

def test_url_gen7():
 # Team 07
 EXCEL_URL_T7 = "https://noaa-goes18.s3.amazonaws.com/ABI-L1b-RadM/2023/003/02/OR_ABI-L1b-RadM1-M6C01_G18_s20230030201252_e20230030201311_c20230030201340.nc"
 test = "OR_ABI-L1b-RadM1-M6C01_G18_s20230030201252_e20230030201311_c20230030201340.nc"
 test_fs_T7 = url_gen_goes(test)
 assert(test_fs_T7 == EXCEL_URL_T7)

def test_url_gen8():
 # Team 08
 EXCEL_URL_T8 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-ACHTF/2022/353/22/OR_ABI-L2-ACHTF-M6_G18_s20223532240210_e20223532249518_c20223532252164.nc"
 test = "OR_ABI-L2-ACHTF-M6_G18_s20223532240210_e20223532249518_c20223532252164.nc"
 test_fs_T8 = url_gen_goes(test)
 assert(test_fs_T8 == EXCEL_URL_T8)

def test_url_gen9():
 # Team 09
 EXCEL_URL_T9 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-DSRC/2022/318/05/OR_ABI-L2-DSRC-M6_G18_s20223180501179_e20223180503552_c20223180508262.nc"
 test = "OR_ABI-L2-DSRC-M6_G18_s20223180501179_e20223180503552_c20223180508262.nc"
 test_fs_T9 = url_gen_goes(test)
 assert(test_fs_T9 == EXCEL_URL_T9)

def test_url_gen10():
 # Team 10
 EXCEL_URL_T10 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-DMWVM/2022/355/20/OR_ABI-L2-DMWVM1-M6C08_G18_s20223552050271_e20223552050328_c20223552122197.nc"
 test = "OR_ABI-L2-DMWVM1-M6C08_G18_s20223552050271_e20223552050328_c20223552122197.nc"
 test_fs_T10 = url_gen_goes(test)
 assert(test_fs_T10 == EXCEL_URL_T10)

def test_url_gen11():
 # Team 11
 EXCEL_URL_T11 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-ACMC/2022/280/09/OR_ABI-L2-ACMC-M6_G18_s20222800931164_e20222800933537_c20222800934574.nc"
 test = "OR_ABI-L2-ACMC-M6_G18_s20222800931164_e20222800933537_c20222800934574.nc"
 test_fs_T11 = url_gen_goes(test)
 assert(test_fs_T11 == EXCEL_URL_T11)

def test_url_gen12():
 # Team 12
 EXCEL_URL_T12 = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-DMWC/2022/351/05/OR_ABI-L2-DMWC-M6C07_G18_s20223510516174_e20223510518559_c20223510527449.nc"
 test = "OR_ABI-L2-DMWC-M6C07_G18_s20223510516174_e20223510518559_c20223510527449.nc"
 test_fs_T12 = url_gen_goes(test)
 assert(test_fs_T12 == EXCEL_URL_T12)