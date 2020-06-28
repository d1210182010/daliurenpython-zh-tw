import datetime
import eacal
from shipan import shipan
from common import Get旺衰, 旺衰
from ganzhiwuxin import 干, 支, 干支
from common import GetLi


def do_伏呤(sp):
    sk = sp.四课
    __支 = sk.支
    __支阳 = sk.支阳神
    if __支 == __支阳:
        sp.setGuaTi("伏吟卦")
        # TODO


def do_返呤(sp):
    sk = sp.四课
    __支 = sk.支
    __支阳 = sk.支阳神
    if (__支 + 6) == __支阳:
        sp.setGuaTi("返吟卦")


def do_龙德(sp):
    __太岁 = sp.四柱与节气[0]
    __月将 = sp.yueJiang
    __三传 = sp.三传
    sc = [__三传.初, __三传.中, __三传.末]
    if sc[0] == __月将 and __太岁.支 in sc:
        sp.setGuaTi("龍德卦")


def do_三光(sp):
    # 2015-08-12 巳将卯时
    __月建 = sp.四柱与节气[1].支
    __三传 = sp.三传
    __初 = __三传.初
    __中 = __三传.中
    __末 = __三传.末
    if Get旺衰(__月建, __初.wuxing) not in [旺衰("旺"), 旺衰("相")]:
        return
    sk = sp.四课
    __干 = sk.干
    __支 = sk.支
    if Get旺衰(__月建, __干.wuxing) not in [旺衰("旺"), 旺衰("相")]:
        return
    if Get旺衰(__月建, __支.wuxing) not in [旺衰("旺"), 旺衰("相")]:
        return
    tj = sp.tianJiang
    c = tj[__初]
    z = tj[__中]
    m = tj[__末]
    if c.吉将 or z.吉将 or m.吉将:
        sp.setGuaTi("三光卦")


def do_三阳(sp):
    # 2018-04-03 戌将 酉时
    __发用 = sp.三传.初
    __月建 = sp.四柱与节气[1].支
    if Get旺衰(__月建, __发用.wuxing) not in [旺衰("旺"), 旺衰("相")]:
        return
    __天将盘 = sp.tianJiang
    if __天将盘.逆:
        return
    sk = sp.四课
    __干 = sk.干
    __支 = sk.支
    __干天将 = __天将盘[shipan.寄宫(__干)]
    __支天将 = __天将盘[__支]
    t = [shipan.天将('蛇'), shipan.天将('雀'), shipan.天将('合'), shipan.天将('勾'),
         shipan.天将('龙')]
    if __干天将 in t and __支天将 in t:
        sp.setGuaTi("三陽卦")


def do_三奇(sp):
    __kw = sp.空亡
    __xs = __kw[1] + 1
    __旬奇 = ""
    if __xs in [支("戌"), 支("子")]:
        __旬奇 = 支("丑")
    if __xs in [支("申"), 支("午")]:
        __旬奇 = 支("子")
    if __xs in [支("寅"), 支("辰")]:
        __旬奇 = 支("亥")

    __sc = sp.三传
    sc = [__sc.初, __sc.中, __sc.末]
    if __旬奇 in sc:
        sp.setGuaTi("三奇卦")


def do_六仪(sp):
    __kw = sp.空亡
    __xs = __kw[1] + 1
    sc = sp.三传
    sc = [sc.初, sc.中, sc.末]
    if __xs in sc:
        sp.setGuaTi("六儀卦")
        return


def do_铸印(sp):
    __三传 = sp.三传
    sc = [__三传.初, __三传.中, __三传.末]
    tp = sp.天盘
    si = 支("巳")
    xu = 支("戌")
    mao = 支("卯")
    if tp[si] != xu:
        return
    if si in sc and xu in sc and mao in sc:
        sp.setGuaTi("鑄印卦")


def do_斫轮(sp):
    sk = sp.四课
    c = sp.三传.初
    tp = sp.天盘
    mao = 支("卯")
    if c != mao:
        return
    __干 = sk.干
    __干上神 = sk.干阳神
    if __干上神 == mao and __干 in [干("庚"), 干("辛")]:
        sp.setGuaTi("斫輪卦")
        return
    lin = tp.临(mao)
    if lin == 支("申") or lin == 支("酉"):
        sp.setGuaTi("斫輪卦")


def do_轩盖(sp):
    __sc = sp.三传
    sc = [__sc.初, __sc.中, __sc.末]
    yin = 支("寅")
    zi = 支("子")
    mao = 支("卯")
    __月建 = sp.四柱与节气[1].支
    tian_ma = 支("午") + (__月建 - yin) * 2
    if zi in sc and mao in sc and tian_ma in sc:
        sp.setGuaTi("軒蓋卦")


def do_官爵(sp):
    __sc = sp.三传
    sc = [__sc.初, __sc.中, __sc.末]
    __戌 = 支("戌")
    if __戌 not in sc:
        return
    tjp = sp.tianJiang
    __太常支 = tjp.临(shipan.天将("常"))
    if __太常支 not in sc:
        return

    zhiList = [sp.四柱与节气[0].支, sp.四柱与节气[1].支, sp.四课.支,
               sp.行年.支, sp.本命.支]
    for i in zhiList:
        zhi = i
        while (zhi - 支("寅")) % 3 != 0:
            zhi = zhi + 4
        yiMa = zhi + 6
        if yiMa in sc:
            sp.setGuaTi("官爵卦")
            return


def do_富贵(sp):
    __发用 = sp.三传.初
    __月建 = sp.四柱与节气[1].支
    if Get旺衰(__月建, __发用.wuxing) not in [旺衰("旺"), 旺衰("相")]:
        return
    tj = sp.tianJiang
    tianYiZhi = tj.临(shipan.天将("贵"))
    if tianYiZhi != __发用:
        return

    tp = sp.天盘
    sk = sp.四课
    __行年上神 = tp[sp.行年.支]
    __本命上神 = tp[sp.本命.支]

    __干上神 = sk.干阳神
    __支上神 = sk.支阳神
    if tianYiZhi in [__行年上神, __本命上神, __干上神, __支上神]:
        sp.setGuaTi("富貴卦")


def do_时泰(sp):
    __太岁 = sp.四柱与节气[0].支
    __发用 = sp.三传.初
    if __发用 != __太岁:
        return
    __月建 = sp.四柱与节气[1].支
    tianYiZhi = sp.tianJiang.临(shipan.天将("龙"))
    if tianYiZhi != __月建:
        return
    __sc = sp.三传
    sc = [__sc.初, __sc.中, __sc.末]
    if __月建 in sc:
        sp.setGuaTi("時泰卦")


def do_九丑(sp):
    sk = sp.四课
    gan =  sk.干
    zhi = sk.支
    if gan not in [干("乙"), 干("戊"), 干("己"), 干("辛"), 干("壬"),]:
        return
    if zhi not in [支("子"), 支("卯"), 支("午"), 支("酉")]:
        return
    __支上神 = sk.支阳神
    if __支上神 != 支("丑"):
        return
    sp.setGuaTi("九丑卦")


def do_二烦(sp):
    sunMansion = sp.yueJiang
    moonMansion = sp. moonMansion
    tp = sp.tp
    sunLing = tp.临(sunMansion)
    moonLing = tp.临(moonMansion)

    if sunLing in [支("子"), 支("卯"), 支("午"), 支("酉")]:
        sp.setGuaTi("天煩卦")

    if moonLing in [支("子"), 支("卯"), 支("午"), 支("酉")]:
        sp.setGuaTi("地煩卦")
    if "天烦卦" in sp.格局 and "地烦卦" in sp.格局:
        sp.setGuaTi("二煩卦")


def do_天祸(sp):
    year = sp.year
    zhanRi = sp.占日

    c = eacal.EACal(zh_s=True)
    liChun = c.get_specified_solar_term(year, 0)[2].replace(tzinfo=None)
    liXiao = c.get_specified_solar_term(year, 6)[2].replace(tzinfo=None)
    liQiu = c.get_specified_solar_term(year, 12)[2].replace(tzinfo=None)
    liDong = c.get_specified_solar_term(year, 18)[2].replace(tzinfo=None)
    t = None
    for i in [liChun, liXiao, liQiu, liDong]:
        t = GetLi(i.year, i.month, i.day, i.hour, i.minute, i.second)[2]
        if t == zhanRi:
            break
    if t is None:
        return
    yesterdayGan = zhanRi + (-1)
    yesterdayJiGong = shipan.寄宫(yesterdayGan.干)
    lin = sp.tp.临(shipan.寄宫(zhanRi.干))
    if yesterdayJiGong == lin:
        sp.setGuaTi("天禍卦")


def do_伏殃(sp):
    __月建 = sp.四柱与节气[1].支
    zhi = __月建
    while (zhi - 支("寅")) % 3 != 0:
        zhi = zhi + 4
    __天鬼 = zhi + 7
    sc = sp.三传
    sk = sp.四课
    tp = sp.天盘
    __chu = sc.初
    __行年上神 = tp[sp.行年.支]
    __本命上神 = tp[sp.本命.支]

    __干上神 = sk.干阳神
    __支上神 = sk.支阳神

    zhiList = [__干上神, __支上神, __chu, __行年上神, __本命上神]
    if __天鬼 in zhiList:
        sp.setGuaTi("伏殃卦")


def do_度厄(sp):
    sk = sp.四课
    __四课 = [sk.一课, sk.二课, sk.三课, sk.四课]
    z = 0
    y = 0
    for i in range(0, 4):
        if __四课[i][0].wuxing.克(__四课[i][1].wuxing):
            z = z + 1
        if __四课[i][1].wuxing.克(__四课[i][0].wuxing):
            y = y + 1
    if z == 3 or y == 3:
        sp.setGuaTi("度厄卦")


def do_无禄绝嗣(sp):
    sk = sp.四课
    __干 = sk.干
    __干阳神 = sk.干阳神
    __干阴神 = sk.干阴神
    __支 = sk.支
    __支阳神 = sk.支阳神
    __支阴神 = sk.支阴神
    if __干阳神.wuxing.克(__干.wuxing) and __干阴神.克(__干阳神) and __支阳神.克(__支) and \
            __支阴神.克(__支阳神):
        sp.setGuaTi("無祿絕嗣卦")
        return
    if __干.wuxing.克(__干阳神.wuxing) and __干阳神.克(__干阴神) and __支.克(__支阳神) and \
            __支阳神.克(__支阴神):
        sp.setGuaTi("無祿絕嗣卦")
        return


def do_罗网(sp):
    sc = sp.三传
    sk = sp.四课
    tp = sp.天盘
    __chu = sc.初
    __行年上神 = tp[sp.行年.支]
    __本命上神 = tp[sp.本命.支]

    __干上神 = sk.干阳神
    __支上神 = sk.支阳神

    zhiList = [__干上神, __支上神, __chu, __行年上神, __本命上神]
    __天罗 = shipan.寄宫(sk.干) + 1
    __地网 = __天罗 + 6

    if __天罗 in zhiList or __地网 in zhiList:
        sp.setGuaTi("羅網卦")


def do__微服(sp):
    sk = sp.四课
    __干阳神 = sk.干阳神
    __干阴神 = sk.干阴神
    __支阳神 = sk.支阳神
    __支阴神 = sk.支阴神
    天将盘 = sp.tianJiang

    __干阳天将 = 天将盘[__干阳神]
    __干阴天将 = 天将盘[__干阴神]
    __支阳天将 = 天将盘[__支阳神]
    __支阴天将 = 天将盘[__支阴神]
    t = [shipan.天将('蛇'), shipan.天将('雀'), shipan.天将('合'), shipan.天将('勾'),
         shipan.天将('龙')]
    if (__干阳天将 not in t) and (__支阳天将 not in t) and \
            (__干阴天将 in t) and (__支阴天将 in t):
        sp.setGuaTi("微服卦")


def do_连珠(sp):
    sc = sp.三传
    if (sc.初 - 支("寅")) % 3 == 0 and sc.初 + 1 == sc.中 and sc.中 + 1 == sc.末:
        sp.setGuaTi("連珠卦")
        return
    if (sc.初 - 支("辰")) % 3 == 0 and sc.初 == sc.中 + 1 and sc.中 == sc.末 + 1:
        sp.setGuaTi("連珠卦")
        return
    y = sp.四柱与节气[0].支
    m = sp.四柱与节气[1].支
    d = sp.四柱与节气[2].支
    if y == sc.初 and m == sc.中 and d == sc.末:
        sp.setGuaTi("連珠卦")
        return
    if d == sc.初 and m == sc.中 and y == sc.末:
        sp.setGuaTi("連珠卦")


def do_连茹(sp):
    sc = sp.三传
    c = sc.初
    z = sc.中
    m = sc.末
    if c + 1 == z and z + 1 == m:
        sp.setGuaTi("連茹卦")
        return
    if c == z + 1 and z == m + 1:
        sp.setGuaTi("連茹卦")


def do_侵害(sp):
    pass
