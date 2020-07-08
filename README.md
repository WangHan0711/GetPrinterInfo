# GetPrinterInfo
基于Python获取一些打印机简单信息

通过TCP连接打印机9100端口，使用PJL语言获取信息，因此打印机需支持PJL语言。

使用方法：```python GetPrinterInfo.py 打印机IP```

实际使用如下：
```shell
root@ids:~# python GetPrinterInfo.py 10.255.88.11
@PJL INFO ID
"Lenovo LJ2250N:84UA03:Ver3.06"

@PJL INFO VARIABLES
COPIES=1 [2 RANGE]
        1
        999
LPARM:PCL PAPER=A4 [17 ENUMERATED]
        LETTER
        LEGAL
        A4
        EXECUTIVE
        COM10
        MONARCH
        C5
        DL
        DLL
        B5
        A5
        A6
        B6
        JISB5
        A4LONG
        POSTCARD
        FOLIO
LPARM:PCL ORIENTATION=PORTRAIT [2 ENUMERATED]
        PORTRAIT
        LANDSCAPE
LPARM:PCL FORMLINES=64 [2 RANGE]
        5
        128
MANUALFEED=OFF [2 ENUMERATED]
        OFF
        ON
PAGEPROTECT=AUTO [5 ENUMERATED]
        OFF
        LETTER
        LEGAL
        A4
        AUTO
RESOLUTION=600 [3 ENUMERATED]
        300
        600
        1200
PERSONALITY=PCL [1 ENUMERATED]
        PCL
TIMEOUT=5 [2 RANGE]
        1
        99
AUTOCONT=OFF [2 ENUMERATED]
        OFF
        ON
CPLOCK=OFF [2 ENUMERATED]
        OFF
        ON
PASSWORD=DISABLED [2 RANGE]
        0
        65535
LANG=ENGLISH [19 ENUMERATED]
        ENGLISH
        FRENCH
        GERMAN
        DUTCH
        SPANISH
        ITALIAN
        FINNISH
        NORWEGIAN
        PORTUGUESE
        DANISH
        JAPANESE
        SWEDISH
        RUSSIAN
        CZECH
        HUNGARIAN
        POLISH
        BULGARIAN
        ROMANIAN
        SLOVAKIAN
AUTOSLEEP=ON [2 ENUMERATED]
        OFF
        ON
TIMEOUTSLEEP=5 [2 RANGE]
        1
        99
POWERSAVE=ON [2 ENUMERATED]
        OFF
        ON
POWERSAVETIME=5 [2 RANGE]
        1
        99
ECONOMODE=OFF [2 ENUMERATED]
        OFF
        ON
ECONOLEVEL=1 [2 RANGE]
        0
        3
MEDIATYPE=THIN [10 ENUMERATED]
        REGULAR
        THICK
        THICK2
        TRANSPARENCY
        THIN
        BOND
        ENVELOPES
        ENVTHICK
        ENVTHIN
        RECYCLED
IMAGEADAPT=ON [3 ENUMERATED]
        OFF
        ON
        AUTO
LPARM:PCL FONTSOURCE=I [1 ENUMERATED]
        I
LPARM:PCL FONTNUMBER=42 [2 RANGE]
        0
        54
LPARM:PCL PITCH=10.00 [2 RANGE]
        0.44
        99.99
LPARM:PCL PTSIZE=12.00 [2 RANGE]
        4.00
        999.75
LPARM:PCL SYMSET=PC8 [80 ENUMERATED]
        PC8
        PC8DN
        PC850
        PC852
        PC8TK
        PC1004
        WINL1
        WINL2
        WINL5
        WINBALT
        DESKTOP
        PSTEXT
        VNINTL
        VNUS
        MSPUBL
        MATH8
        PSMATH
        VNMATH
        PIFONT
        LEGAL
        ISO2
        ISO4
        ISO6
        ISO10
        ISO11
        ISO14
        ISO15
        ISO16
        ISO17
        ISO21
        ISO25
        ISO57
        ISO60
        ISO61
        ISO69
        ISO84
        ISO85
        WIN30
        HPGERM
        HPSPAN
        MCTEXT
        SYMBOL
        OCRA
        OCRB
        WDINGS
        HEBREW7
        ROMAN8
        ISOL1
        ISOL2
        ISOL5
        ISOL6
        PC775
        ABIBP
        ABIINTL
        RUSSIAN
        UKRAINIAN
        PC866
        PC8LG
        PC851
        WINGREEK
        ISOLC
        ISOGREEK
        PC853
        PC855
        PC857
        PC858
        PC860
        PC861
        PC863
        PC865
        PC869
        ISOL9
        PC8B
        PC8G
        PC8PC
        GREEK8
        TURKISH8
        ROMAN9
        ROMANEXT
        WINC
INTRAY2=UNLOCKED [2 ENUMERATED READONLY]
        UNLOCKED
        LOCKED
SOURCETRAY=AUTO [2 ENUMERATED]
        AUTO
        TRAY1
LPARM:PCL LEFTMARGIN=0 [2 RANGE]
        0
        145
LPARM:PCL RIGHTMARGIN=78 [2 RANGE]
        10
        155
LPARM:PCL TOPMARGIN=0.50 [2 RANGE]
        0.00
        2.00
LPARM:PCL BOTMARGIN=0.50 [2 RANGE]
        0.00
        2.00
XOFFSET=0 [2 RANGE]
        -500
        500
YOFFSET=0 [2 RANGE]
        -500
        500
LPARM:PCL AUTOLF=OFF [2 ENUMERATED]
        OFF
        ON
LPARM:PCL AUTOCR=OFF [2 ENUMERATED]
        OFF
        ON
LPARM:PCL AUTOWRAP=OFF [2 ENUMERATED]
        OFF
        ON
LPARM:PCL AUTOSKIP=ON [2 ENUMERATED]
        OFF
        ON
AUTOFF=OFF [2 ENUMERATED]
        OFF
        ON
TIMEOUTFF=5 [2 RANGE]
        1
        99
FFSUPPRESS=OFF [2 ENUMERATED]
        OFF
        ON
DEMOPRINT=OFF [2 ENUMERATED]
        OFF
        ON
DOWNFPROD=OFF [2 ENUMERATED]
        OFF
        ON
BITMAPFPROD=ON [2 ENUMERATED]
        OFF
        ON
OEMFONT=OFF [2 ENUMERATED]
        OFF
        ON
DARKFONT=OFF [2 ENUMERATED]
        OFF
        ON
COMPABITMAP=OFF [2 ENUMERATED]
        OFF
        ON
FSEL300DPI=LOW [2 ENUMERATED]
        LOW
        HIGH
DEFPAPER=A4 [2 ENUMERATED]
        A4
        LETTER
HPESCE=RESET [2 ENUMERATED]
        RESET
        FF
PROTECTOFF=AUTO [2 ENUMERATED]
        AUTO
        NORMAL
RAS1200MODE=OFF [3 ENUMERATED]
        OFF
        ON
        TRUE
DENSITY=0 [2 RANGE]
        -6
        6
ISRFONT=OFF [2 ENUMERATED]
        OFF
        ON
TRANSFER=AUTO [3 ENUMERATED]
        AUTO
        LOW
        HIGH
DOUBLESTRIKE=OFF [2 ENUMERATED]
        OFF
        ON
ERRORPRINT=ON [3 ENUMERATED]
        OFF
        ON
        EXCEPTCDCC
DEMOLANG=ENGLISH [8 ENUMERATED]
        ENGLISH
        USA
        CANADA
        FRENCHDUTCH
        GERMANFRENCH
        SPANISHPORTUGUESE
        ITALIAN
        NORDIC
STRINGCODESET=HPROMAN8 [4 ENUMERATED]
        HPROMAN8
        ISO88592
        ISO88595
        JISX02011976
LESSPAPERCURL=OFF [2 ENUMERATED]
        OFF
        ON
FIXINTENSITYUP=OFF [2 ENUMERATED]
        OFF
        ON
DENSITYLEVELUP=OFF [2 ENUMERATED]
        OFF
        ON
ENABLEEMAILREPORTS=OFF [2 ENUMERATED]
        OFF
        ON

@PJL INFO CONFIG
IN TRAYS [2 ENUMERATED]
        INTRAY1 MP
        INTRAY2 PC
OUT TRAYS [1 ENUMERATED]
        NORMAL FACEDOWN
PAPERS [17 ENUMERATED]
        LETTER
        LEGAL
        FOLIO
        EXECUTIVE
        A4
        A5
        A6
        JISB5
        B5
        B6
        A4LONG
        COM10
        MONARCH
        C5
        DL
        DLL
        POSTCARD
LANGUAGES [2 ENUMERATED]
        PCL
        PCLXL
USTATUS [4 ENUMERATED]
        DEVICE
        JOB
        PAGE
        TIMED
MEMORY=16777216
DISPLAY LINES=1
DISPLAY CHARACTER SIZE=16
LOCAL=ENGLISH
FEATURES [5 ENUMERATED]
        USB
        R600
        PAGEP
        DLF0
        BRNET

@PJL INFO MEMORY
TOTAL=8380032
LARGEST=8380032

@PJL INFO PAGECOUNT
PAGECOUNT=103904

@PJL INFO STATUS
CODE=10001
DISPLAY="READY           "
ONLINE=TRUE


root@ids:~#

```
