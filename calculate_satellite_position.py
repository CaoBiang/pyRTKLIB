# https://github.com/CaoBiang/pyRTKLIB
import math

def calculate_satellite_position(brdcParameter):
    
    pi=3.14159265358979323846
    omegae = 7.2921151467e-5
    mu = 3.986005e14
    
    # 建立星历参数列表
    toe = brdcParameter[0]
    sqrta = brdcParameter[1]
    e = brdcParameter[2]
    i0 = brdcParameter[3]
    omega0 = brdcParameter[4]
    omega = brdcParameter[5]
    m0 = brdcParameter[6]
    deltan = brdcParameter[7]
    idot = brdcParameter[8]
    omegadot = brdcParameter[9]
    Cuc = brdcParameter[10]
    Cus = brdcParameter[11]
    Crc = brdcParameter[12]
    Crs = brdcParameter[13]
    Cic = brdcParameter[14]
    Cis = brdcParameter[15]
    tk = brdcParameter[16]

    # 计算卫星位置
    A = sqrta ** 2  # 卫星轨道半长轴
    n_0 = math.sqrt(mu / A ** 3)  # 卫星平均角速度
    n = n_0 + deltan  # 校正后的卫星平均角速度
    # 平近点角（迭代法）
    Mk = m0 + n * tk
    if Mk < 0:
        Mk += 2 * math.pi
    if Mk > 2 * math.pi:
        Mk -= 2 * math.pi
    # 偏近点角
    Eold = Mk
    Enew = Mk + e * math.sin(Eold)
    j = 1

    while abs(Enew - Eold) > 1e-8:
        Eold = Enew
        Enew = Mk + e * math.sin(Eold)
        j += 1
        if (j > 10):
            break

    Ek = Enew

    # 真近点角
    cosNuk = (math.cos(Ek) - e) / (1 - e * math.cos(Ek))
    sinNuk = (math.sqrt(1 - e ** 2) * math.sin(Ek)) / (1 - e * math.cos(Ek))

    Nk = math.atan(sinNuk / cosNuk)
    #结局真近点角象限不同出现的取值异常情况
    if cosNuk < 0 :
        Nk += math.pi
    #升交点角距
    Pk = Nk + omega

    deltauk = Cus * math.sin(2 * Pk) + Cuc * math.cos(2 * Pk)
    deltark = Crs * math.sin(2 * Pk) + Crc * math.cos(2 * Pk)
    deltaik = Cis * math.sin(2 * Pk) + Cic * math.cos(2 * Pk)
    #摄动改正后升交点角距、卫星矢径长度、轨道倾角
    uk = Pk + deltauk
    rk = A * (1 - e * math.cos(Ek)) + deltark
    ik = i0 + idot * tk + deltaik
    #极坐标转化为直角坐标
    x1k = rk * math.cos(uk)
    y1k = rk * math.sin(uk)
    #升交点赤经
    omegak = omega0 + (omegadot - omegae) * tk - omegae * toe
    #最终WGS84坐标
    xk = x1k * math.cos(omegak) - y1k * math.cos(ik) * math.sin(omegak)
    yk = x1k * math.sin(omegak) + y1k * math.cos(ik) * math.cos(omegak)
    zk = y1k * math.sin(ik)

    SatellitePosition=[xk,yk,zk]
    return SatellitePosition


