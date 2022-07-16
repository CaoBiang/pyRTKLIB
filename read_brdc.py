# https://github.com/CaoBiang/pyRTKLIB

import linecache


def read_brdc(brdc_name='brdc0010.20n', satellite_name='5'):
    satellite_time_h = []
    satellite_time_m = []
    satellite_time_s = []
    toe = []
    sqrta = []
    e = []
    i0 = []
    omega0 = []
    omega = []
    m0 = []
    deltan = []
    idot = []
    omegadot = []
    Cuc = []
    Cus = []
    Crc = []
    Crs = []
    Cic = []
    Cis = []

    # 头文件有多少行
    head_count = 8
    # 一共多少行
    all_count = len(open(brdc_name).readlines())
    # 读取广播星历文件参数
    all_satellite_first_line = [i + head_count for i in list(range(1, all_count - 1, 8))]  # 每次观测第一行在广播星历中的行数

    choosen_satellite_first_line = []  # 所需卫星每次观测在广播星历文件中的第一行

    for i in all_satellite_first_line:  #
        read_line = linecache.getline(brdc_name, i).strip()  # 读取所有卫星每次观测的第一行
        satellite_number = read_line[0:2].replace(' ', '')  # 截取开头的两个字符，为卫星编号
        if satellite_number == satellite_name:  # 如果卫编号刚好符合我们需要求的卫星编号，便把这一行数记录下来
            choosen_satellite_first_line.append(i)
    print(choosen_satellite_first_line)

    # 根据广播星历参数的排列顺序分别读取各个参数并加入列表
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 3).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            toe1 = float(read_line[0:15])
            toe2 = float(read_line[16:19])
        else:
            toe1 = float(read_line[0:14])
            toe2 = float(read_line[15:18])
        toe.append(toe1 * 10 ** toe2)

    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 2).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            e1 = float(read_line[19:34])
            e2 = float(read_line[35:38])
        else:
            e1 = float(read_line[18:33])
            e2 = float(read_line[34:37])
        e.append(e1 * 10 ** e2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 4).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            i01 = float(read_line[0:15])
            i02 = float(read_line[16:19])
        else:
            i01 = float(read_line[0:14])
            i02 = float(read_line[15:18])
        i0.append(i01 * 10 ** i02)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 4).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            omega1 = float(read_line[38:53])
            omega2 = float(read_line[54:57])
        else:
            omega1 = float(read_line[37:52])
            omega2 = float(read_line[53:56])
        omega.append(omega1 * 10 ** omega2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 3).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            omega01 = float(read_line[38:53])
            omega02 = float(read_line[54:57])
        else:
            omega01 = float(read_line[37:52])
            omega02 = float(read_line[53:56])
        omega0.append(omega01 * 10 ** omega02)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 1).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            mu01 = float(read_line[57:72])
            mu02 = float(read_line[73:76])
        else:
            mu01 = float(read_line[56:71])
            mu02 = float(read_line[72:75])
        m0.append(mu01 * 10 ** mu02)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 1).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            delten1 = float(read_line[38:53])
            delten2 = float(read_line[54:57])
        else:
            delten1 = float(read_line[37:52])
            delten2 = float(read_line[53:56])
        deltan.append(delten1 * 10 ** delten2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 4).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            omegadot1 = float(read_line[57:72])
            omegadot2 = float(read_line[73:76])
        else:
            omegadot1 = float(read_line[56:71])
            omegadot2 = float(read_line[72:75])
        omegadot.append(omegadot1 * 10 ** omegadot2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 5).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            idot1 = float(read_line[0:15])
            idot2 = float(read_line[16:19])
        else:
            idot1 = float(read_line[0:14])
            idot2 = float(read_line[15:18])
        idot.append(idot1 * 10 ** idot2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 2).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            cus1 = float(read_line[38:53])
            cus2 = float(read_line[54:57])
        else:
            cus1 = float(read_line[37:52])
            cus2 = float(read_line[53:56])
        Cus.append(cus1 * 10 ** cus2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 2).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            cuc1 = float(read_line[0:15])
            cuc2 = float(read_line[16:19])
        else:
            cuc1 = float(read_line[0:14])
            cuc2 = float(read_line[15:18])
        Cuc.append(cuc1 * 10 ** cuc2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 3).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            cis1 = float(read_line[57:72])
            cis2 = float(read_line[73:76])
        else:
            cis1 = float(read_line[56:71])
            cis2 = float(read_line[72:75])
        Cis.append(cis1 * 10 ** cis2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 3).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            cic1 = float(read_line[19:34])
            cic2 = float(read_line[35:38])
        else:
            cic1 = float(read_line[18:33])
            cic2 = float(read_line[34:37])
        Cic.append(cic1 * 10 ** cic2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 1).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            crs1 = float(read_line[19:34])
            crs2 = float(read_line[35:38])
        else:
            crs1 = float(read_line[18:33])
            crs2 = float(read_line[34:37])
        Crs.append(crs1 * 10 ** crs2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 4).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            crc1 = float(read_line[19:34])
            crc2 = float(read_line[35:38])
        else:
            crc1 = float(read_line[18:33])
            crc2 = float(read_line[34:37])
        Crc.append(crc1 * 10 ** crc2)
    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i + 2).strip()
        mole = float(read_line[0:5])
        if mole < 0:
            sqra1 = float(read_line[57:72])
            sqra2 = float(read_line[73:76])
        else:
            sqra1 = float(read_line[56:71])
            sqra2 = float(read_line[72:75])
        sqrta.append(sqra1 * 10 ** sqra2)

    for i in choosen_satellite_first_line:
        read_line = linecache.getline(brdc_name, i).strip()
        if len(satellite_name) == 1:
            h = read_line[11:13]
            m = read_line[14:16]
            s = read_line[17:21]
        else:
            h = read_line[12:14]
            m = read_line[15:17]
            s = read_line[18:22]
        satellite_time_h.append(h.lstrip())
        satellite_time_m.append(m.lstrip())
        satellite_time_s.append(s.lstrip())
        satellite_time_h = list(map(int, satellite_time_h))  # 字符串转浮点数
        satellite_time_m = list(map(int, satellite_time_m))
        satellite_time_s = list(map(float, satellite_time_s))


read_brdc()
