import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):


    def test101(self):
        input="""//2nFHWZKpPugkMvJd //?ascjkas{.+naisj
///Rdobt6fz79#b6hB=Dm1<u3]C3MxpdcPcDav8
//"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 101))


    def test102(self):
        input="""/**/ /*lRVxOcIAMf4xrKI7Qv2t*/
/*
AaBbCcascklasnckascn
[]}{P\:',.}
*/"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 102))


    def test103(self):
        input="""abcdefghijklmnopqrstuvwxyz qokdnhzasrltbevypwjucximgf  nzcoujaskxyrehwpgvmbqflitd"""
        expect="""abcdefghijklmnopqrstuvwxyz,qokdnhzasrltbevypwjucximgf,nzcoujaskxyrehwpgvmbqflitd,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 103))


    def test104(self):
        input="""vcusuwxzhalelhf
jvdocodruuatdoj
sdryfcuspalczdb
fkhftpxfptcurwp"""
        expect="""vcusuwxzhalelhf,jvdocodruuatdoj,sdryfcuspalczdb,fkhftpxfptcurwp,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 104))


    def test105(self):
        input="""ABCDEFGHIJKLMNOPQRSTUVWXYZ XJVOKULBENTYCPMFGWRDZQAHSI   VHLNMSWKZRGUICETBYOAQDFPXJ"""
        expect="""ABCDEFGHIJKLMNOPQRSTUVWXYZ,XJVOKULBENTYCPMFGWRDZQAHSI,VHLNMSWKZRGUICETBYOAQDFPXJ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 105))


    def test106(self):
        input="""UKZGNTBTTSESXTBXRW
XASBCTJYJVBERTHQWI
UWJJCHKRVTYZKQRXPA
SAHTYLIFDCRMFRODBL
NSXYZYHMJUPDTPGUJQ
PXFDTKJTEHOSPMIVIP"""
        expect="""UKZGNTBTTSESXTBXRW,XASBCTJYJVBERTHQWI,UWJJCHKRVTYZKQRXPA,SAHTYLIFDCRMFRODBL,NSXYZYHMJUPDTPGUJQ,PXFDTKJTEHOSPMIVIP,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 106))


    def test107(self):
        input="""________ ___________ ___"""
        expect="""________,___________,___,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 107))


    def test108(self):
        input="""a828073658815 D52 _76258454570972289786"""
        expect="""a828073658815,D52,_76258454570972289786,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 108))


    def test109(self):
        input="""VB7rQHEGDGp88mx iA_anAuBR0FLt2C ac_UP18cK5zOE9l"""
        expect="""VB7rQHEGDGp88mx,iA_anAuBR0FLt2C,ac_UP18cK5zOE9l,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 109))


    def test110(self):
        input="""RP4Zv2yA QGiIaW6x _wcfhP"""
        expect="""RP4Zv2yA,QGiIaW6x,_wcfhP,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 110))


    def test111(self):
        input="""g4CVxYSdr __o65yS33fh sGUqcsTti"""
        expect="""g4CVxYSdr,__o65yS33fh,sGUqcsTti,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 111))


    def test112(self):
        input="""EsV3 _8N0MRxCXjB aXJEYJuGWZzBM1Q qBK_y0OEqhYA56268TY4YDGixQp1Y5"""
        expect="""EsV3,_8N0MRxCXjB,aXJEYJuGWZzBM1Q,qBK_y0OEqhYA56268TY4YDGixQp1Y5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 112))


    def test113(self):
        input="""auto break boolean do else false float for function if integer return string true while void out continue of inherit array"""
        expect="""auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 113))


    def test114(self):
        input="""dO TrUe whilE false VOId function oUt CONTINuE OF while INHErIT"""
        expect="""dO,TrUe,whilE,false,VOId,function,oUt,CONTINuE,OF,while,INHErIT,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 114))


    def test115(self):
        input="""elsE INteG3r FLOAT Of ArRayIF FALSe bOoLEaN InherIt TRUE FoR coNTinue StRinG"""
        expect="""elsE,INteG3r,FLOAT,Of,ArRayIF,FALSe,bOoLEaN,InherIt,TRUE,FoR,coNTinue,StRinG,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 115))


    def test116(self):
        input="""iNhERiT STring 87function retuRN 45_67do trUe 123auto"""
        expect="""iNhERiT,STring,87,function,retuRN,4567,do,trUe,123,auto,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 116))


    def test117(self):
        input="""4_27.89inherit string FUNCTION 2.24return do trUe auto array 7.E-10continue bREak"""
        expect="""427.89,inherit,string,FUNCTION,2.24,return,do,trUe,auto,array,7.E-10,continue,bREak,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 117))


    def test118(self):
        input="""12for 34while 56continue 78integer .02E+4boolean 82_52array trUE void do"""
        expect="""12,for,34,while,56,continue,78,integer,.02E+4,boolean,8252,array,trUE,void,do,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 118))


    def test119(self):
        input="""breakfalse stringof forwhile continueinteger booleanarray truevoid dofloatauto elseifout returninheritfunction"""
        expect="""breakfalse,stringof,forwhile,continueinteger,booleanarray,truevoid,dofloatauto,elseifout,returninheritfunction,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 119))


    def test120(self):
        input="""array 5_27integer 0.e-8for fUnCtION aUto of false 45break inheritout void contInue flOAT do"""
        expect="""array,527,integer,0.e-8,for,fUnCtION,aUto,of,false,45,break,inheritout,void,contInue,flOAT,do,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 120))


    def test121(self):
        input="""{2,5,7}return wHIle fLoAT BOolEan IF 829137128937continue integer"""
        expect="""{,2,,,5,,,7,},return,wHIle,fLoAT,BOolEan,IF,829137128937,continue,integer,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 121))


    def test122(self):
        input="""for whileelsebreak aRRay 4567auto 2.03return out do 8E-10string conTInuE if {1,2}false flOAt 29true b00lEAn functionof .0e+2void integer inherit"""
        expect="""for,whileelsebreak,aRRay,4567,auto,2.03,return,out,do,8E-10,string,conTInuE,if,{,1,,,2,},false,flOAt,29,true,b00lEAn,functionof,.0e+2,void,integer,inherit,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 122))


    def test123(self):
        input="""+ - ! != - && < * || <=  / == > % >= ::"""
        expect="""+,-,!,!=,-,&&,<,*,||,<=,/,==,>,%,>=,::,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))


    def test124(self):
        input="""297edl+_kajsnc-1238.29*iNte/scaas2%287kmaAlSc!abcde&&mnpqrs||casjkcn==ioqw2179_!=aS82nY<tInchuAnchUaAnh<=__chU3nNh3>chiTh0Ngoc>=NhuTh3lAquaIt::"""
        expect="""297,edl,+,_kajsnc,-,1238.29,*,iNte,/,scaas2,%,287,kmaAlSc,!,abcde,&&,mnpqrs,||,casjkcn,==,ioqw2179_,!=,aS82nY,<,tInchuAnchUaAnh,<=,__chU3nNh3,>,chiTh0Ngoc,>=,NhuTh3lAquaIt,::,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 124))


    def test125(self):
        input="""edl+kajsnc-1238.29*iNte/sca"""
        expect="""edl,+,kajsnc,-,1238.29,*,iNte,/,sca,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 125))


    def test126(self):
        input="""pmhjn9%073qhaKjW!hijkl&&stuvw"""
        expect="""pmhjn9,%,0,73,qhaKjW,!,hijkl,&&,stuvw,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 126))


    def test127(self):
        input="""cvbn==gjkl0876!=bX86fR<vRkghItrgkIjTrgk<=__rgk3bBk3"""
        expect="""cvbn,==,gjkl0876,!=,bX86fR,<,vRkghItrgkIjTrgk,<=,__rgk3bBk3,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 127))


    def test128(self):
        input="""179!=aS82nY<tInchuAnchUaAnh<=__chU3nNh3>chiTh0Ngoc>=NhuTh"""
        expect="""179,!=,aS82nY,<,tInchuAnchUaAnh,<=,__chU3nNh3,>,chiTh0Ngoc,>=,NhuTh,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 128))


    def test129(self):
        input="""FqrbKlqrbOlqrb<=__lqrb9jJj9>lqrzQk6Rqrb>=JjkQk6GAquaIt::2.07e-10"""
        expect="""FqrbKlqrbOlqrb,<=,__lqrb9jJj9,>,lqrzQk6Rqrb,>=,JjkQk6GAquaIt,::,2.07e-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 129))


    def test130(self):
        input="""plus +sub -negat3!=_different!"""
        expect="""plus,+,sub,-,negat3,!=,_different,!,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 130))


    def test131(self):
        input="""-substract and&&and leq<=leq le<le _mul*Mul OrOp||OrOp"""
        expect="""-,substract,and,&&,and,leq,<=,leq,le,<,le,_mul,*,Mul,OrOp,||,OrOp,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 131))


    def test132(self):
        input="""div/dived equal== 123Greater> Mod%m0d geq>=129.86geq j0in::_concat"""
        expect="""div,/,dived,equal,==,123,Greater,>,Mod,%,m0d,geq,>=,129.86,geq,j0in,::,_concat,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 132))


    def test133(self):
        input="""( ) [ ] . , ; : { } ="""
        expect="""(,),[,],.,,,;,:,{,},=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 133))


    def test134(self):
        input="""(some_exp) abc][xyz int.float ele,ele assignment; identifier:value {index1 index2 index3} 4=12_52.e8"""
        expect="""(,some_exp,),abc,],[,xyz,int,.,float,ele,,,ele,assignment,;,identifier,:,value,{,index1,index2,index3,},4,=,1252.e8,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 134))


    def test135(self):
        input="""N]xIuI)E;Bid2On3 eiIB[1:=4()n9wuQ}T47 jY(ZhnEG4sCmhuInNNqO"""
        expect="""N,],xIuI,),E,;,Bid2On3,eiIB,[,1,:,=,4,(,),n9wuQ,},T47,jY,(,ZhnEG4sCmhuInNNqO,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 135))


    def test136(self):
        input="""0 8362036934498436585 385753_4_93618 2_3 """
        expect="""0,8362036934498436585,385753493618,23,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 136))


    def test137(self):
        input="""298_128 1__23918 82710"""
        expect="""298128,1,__23918,82710,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 137))


    def test138(self):
        input="""7432.901 9_1.641 0.518202"""
        expect="""7432.901,91.641,0.518202,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 138))


    def test139(self):
        input="""5_667E0 947_8E+2 2E-77 1_0652e6 8e+3479 28e-9"""
        expect="""5667E0,9478E+2,2E-77,10652e6,8e+3479,28e-9,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 139))


    def test140(self):
        input="""72.E-28 128_230.E+1298 82_3.E7 217.e7 46.e+8 2_19.e-9"""
        expect="""72.E-28,128230.E+1298,823.E7,217.e7,46.e+8,219.e-9,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 140))


    def test141(self):
        input=""".1289E10 .0002E+4 .86E-4 .271e9 .11111e+74 .721e-47"""
        expect=""".1289E10,.0002E+4,.86E-4,.271e9,.11111e+74,.721e-47,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 141))


    def test142(self):
        input="""7.8E9 28.0E-2 21_98.127E+28 123_456_789.002e2 7231_1.712e+128 81.01299e-10"""
        expect="""7.8E9,28.0E-2,2198.127E+28,123456789.002e2,72311.712e+128,81.01299e-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 142))


    def test143(self):
        input="""827_123712 .82e+27 1.2 2_8310.E-28 281E-89"""
        expect="""827123712,.82e+27,1.2,28310.E-28,281E-89,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 143))


    def test144(self):
        input="""2.E82 8.0e-20 0 78_910 9.2e+92 .162E-10"""
        expect="""2.E82,8.0e-20,0,78910,9.2e+92,.162E-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 144))


    def test145(self):
        input="""281 8_3912.0 72.e19 4_567_819.123456 12.E-0 11.1E+2"""
        expect="""281,83912.0,72.e19,4567819.123456,12.E-0,11.1E+2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 145))


    def test146(self):
        input="""true false True tRUe+false abcd::false"""
        expect="""true,false,True,tRUe,+,false,abcd,::,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146))


    def test147(self):
        input=""" "" """
        expect=""",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 147))


    def test148(self):
        input=""" "The lake is a long way from here." """
        expect="""The lake is a long way from here.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 148))


    def test149(self):
        input=""" "Today we gathered moss for my uncle\\'s wedding." """
        expect="""Today we gathered moss for my uncle\\'s wedding.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 149))


    def test150(self):
        input=""" "A glittering \\t gem is not enough" """
        expect="""A glittering \\t gem is not enough,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 150))


    def test151(self):
        input=""" "We have \\t a lot of rain in June *12983?/" """
        expect="""We have \\t a lot of rain in June *12983?/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 151))


    def test152(self):
        input=""" "abc \\"abc1!!@#$$%^i" """
        expect="""abc \\"abc1!!@#$$%^i,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 152))


    def test153(self):
        input=""" "\tYou have every right to be angry " """
        expect="""	You have every right to be angry ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 153))


    def test154(self):
        input=""" "John walks out and said: \\"What a lovely day!\\"" """
        expect="""John walks out and said: \\"What a lovely day!\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 154))


    def test155(self):
        input=""" "128canbsjk *+-=- \\" something_r@nd$m &^%\\"" """
        expect="""128canbsjk *+-=- \\" something_r@nd$m &^%\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 155))


    def test156(self):
        input=""" "12d*1283 \\"1289eyu12\\"  ka1209@#@%^ \\" hmm \\"" """
        expect="""12d*1283 \\"1289eyu12\\"  ka1209@#@%^ \\" hmm \\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 156))


    def test157(self):
        input=""" "\\"!=$5F!6\\"_}|q\\"!SQBST,H}\\"sIfpw" """
        expect="""\\"!=$5F!6\\"_}|q\\"!SQBST,H}\\"sIfpw,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157))


    def test158(self):
        input=""" "1.20e^219 .2e+10 E7^@(;'.,)\\b \\t \\n \\r \\f \\\\" """
        expect="""1.20e^219 .2e+10 E7^@(;'.,)\\b \\t \\n \\r \\f \\\\,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))


    def test159(self):
        input=""" "Hello, how are you? \\"I\\'m fine, thank you and you\\"" """
        expect="""Hello, how are you? \\"I\\'m fine, thank you and you\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 159))


    def test160(self):
        input=""" "\\"This \\b is \\n the \\f final \\t test \\r \\" ma\\'am" """
        expect="""\\"This \\b is \\n the \\f final \\t test \\r \\" ma\\'am,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160))


    def test161(self):
        input=""" "abcxyz """
        expect="""Unclosed String: abcxyz """
        self.assertTrue(TestLexer.test(input, expect, 161))


    def test162(self):
        input="""r_andom_string+! " this is unclosed string"""
        expect="""r_andom_string,+,!,Unclosed String:  this is unclosed string"""
        self.assertTrue(TestLexer.test(input, expect, 162))


    def test163(self):
        input=""" "!@#^# jnasc \\" nothing here \\" !@#!1283912"""
        expect="""Unclosed String: !@#^# jnasc \\" nothing here \\" !@#!1283912"""
        self.assertTrue(TestLexer.test(input, expect, 163))


    def test164(self):
        input="""{cjknc}"XFS;\nH2\"@hB*\\"cg\\"tA1"""
        expect="""{,cjknc,},Unclosed String: XFS;"""
        self.assertTrue(TestLexer.test(input, expect, 164))


    def test165(self):
        input=""" "@8A*\\"128fjabcassc\\"3K1"""
        expect="""Unclosed String: @8A*\\"128fjabcassc\\"3K1"""
        self.assertTrue(TestLexer.test(input, expect, 165))


    def test166(self):
        input="""+-211c2918WfY[]"jy\\"@cm*\\"OCzP1 \\n"""
        expect="""+,-,211,c2918WfY,[,],Unclosed String: jy\\"@cm*\\"OCzP1 \\n"""
        self.assertTrue(TestLexer.test(input, expect, 166))


    def test167(self):
        input="""12.e+2"G&T-;\\"9j\\"@1f*\\tYI\\"QZ1"""
        expect="""12.e+2,Unclosed String: G&T-;\\"9j\\"@1f*\\tYI\\"QZ1"""
        self.assertTrue(TestLexer.test(input, expect, 167))


    def test168(self):
        input=""" "90{12,34,56}\\t\\b\\'"""
        expect="""Unclosed String: 90{12,34,56}\\t\\b\\'"""
        self.assertTrue(TestLexer.test(input, expect, 168))


    def test169(self):
        input="""%;"[#Ffs?0ED\\"T`#!7n"""
        expect="""%,;,Unclosed String: [#Ffs?0ED\\"T`#!7n"""
        self.assertTrue(TestLexer.test(input, expect, 169))


    def test170(self):
        input=""" "Please New Line \n" """
        expect="""Unclosed String: Please New Line """
        self.assertTrue(TestLexer.test(input, expect, 170))


    def test171(self):
        input=""" "First illegal escape \\a" """
        expect="""Illegal Escape In String: First illegal escape \\a"""
        self.assertTrue(TestLexer.test(input, expect, 171))


    def test172(self):
        input=""" ",Want \\"to\\" see \\c you" """
        expect="""Illegal Escape In String: ,Want \\"to\\" see \\c"""
        self.assertTrue(TestLexer.test(input, expect, 172))


    def test173(self):
        input="""123_1298"abcxyz \\m" """
        expect="""1231298,Illegal Escape In String: abcxyz \\m"""
        self.assertTrue(TestLexer.test(input, expect, 173))


    def test174(self):
        input=""" "Something new \\812" """
        expect="""Illegal Escape In String: Something new \\8"""
        self.assertTrue(TestLexer.test(input, expect, 174))


    def test175(self):
        input="""(12218%21)aiosca"\\smnpq \\" ajscn\\" " """
        expect="""(,12218,%,21,),aiosca,Illegal Escape In String: \\s"""
        self.assertTrue(TestLexer.test(input, expect, 175))


    def test176(self):
        input=""" "\\?\\*\\@" """
        expect="""Illegal Escape In String: \\?"""
        self.assertTrue(TestLexer.test(input, expect, 176))


    def test177(self):
        input="""YAD)"srD)[E}w7\\DQwT" """
        expect="""YAD,),Illegal Escape In String: srD)[E}w7\\D"""
        self.assertTrue(TestLexer.test(input, expect, 177))


    def test178(self):
        input=""";upH"+\\+8MP5" """
        expect=""";,upH,Illegal Escape In String: +\\+"""
        self.assertTrue(TestLexer.test(input, expect, 178))


    def test179(self):
        input="""if*Mhymiz"G>=Y+r9[g(Fh)MH\\'qoteZ\\5(Ze>W3pT+" """
        expect="""if,*,Mhymiz,Illegal Escape In String: G>=Y+r9[g(Fh)MH\\'qoteZ\\5"""
        self.assertTrue(TestLexer.test(input, expect, 179))


    def test180(self):
        input="""550>EqDAv{)i("jA\\i:Wyj5{FgJD]9r" """
        expect="""550,>,EqDAv,{,),i,(,Illegal Escape In String: jA\\i"""
        self.assertTrue(TestLexer.test(input, expect, 180))


    def test181(self):
        input="""WDy break M?u>i1/9wFRIp8h<WKYVJ[2"""
        expect="""WDy,break,M,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 181))


    def test182(self):
        input="""break identy 12.02 @"""
        expect="""break,identy,12.02,Error Token @"""
        self.assertTrue(TestLexer.test(input, expect, 182))


    def test183(self):
        input="""a+b-c*d/nacac 1_982 {1,2,3} ($#^)"""
        expect="""a,+,b,-,c,*,d,/,nacac,1982,{,1,,,2,,,3,},(,Error Token $"""
        self.assertTrue(TestLexer.test(input, expect, 183))


    def test184(self):
        input=""" "Meet Yourself" abcdef#"""
        expect="""Meet Yourself,abcdef,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 184))


    def test185(self):
        input="""pQ*6'q0+Y@}f(^9Xn"""
        expect="""pQ,*,6,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 185))


    def test186(self):
        input="""cjknaUncR 28139_1247162 mnqs +-^"""
        expect="""cjknaUncR,281391247162,mnqs,+,-,Error Token ^"""
        self.assertTrue(TestLexer.test(input, expect, 186))


    def test187(self):
        input="""&8Wy&)eXG{e6:y^=PHF&g*L?#"""
        expect="""Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 187))


    def test188(self):
        input="""PJq:S=6(?^=i"""
        expect="""PJq,:,S,=,6,(,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 188))


    def test189(self):
        input="""do while 0TN-jbs)NJnj1^ac$9^"""
        expect="""do,while,0,TN,-,jbs,),NJnj1,Error Token ^"""
        self.assertTrue(TestLexer.test(input, expect, 189))


    def test190(self):
        input="""t66 GI9K integer z8aVC>rKH)FZ{]$3w3eh43+&>IDcyZQ>Q:KF1eLFP5"""
        expect="""t66,GI9K,integer,z8aVC,>,rKH,),FZ,{,],Error Token $"""
        self.assertTrue(TestLexer.test(input, expect, 190))


    def test191(self):
        input="""a,b,c : integer = 3,4,6"""
        expect="""a,,,b,,,c,:,integer,=,3,,,4,,,6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 191))


    def test192(self):
        input=""" " Hello Worlds \\m" """
        expect="""Illegal Escape In String:  Hello Worlds \\m"""
        self.assertTrue(TestLexer.test(input, expect, 192))


    def test193(self):
        input="""MyArray: array [1+2,4+5] of float = {9,10}"""
        expect="""MyArray,:,array,[,1,+,2,,,4,+,5,],of,float,=,{,9,,,10,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 193))


    def test194(self):
        input="""if (x>1) then return foo(x+1) else x= "\\a" """
        expect="""if,(,x,>,1,),then,return,foo,(,x,+,1,),else,x,=,Illegal Escape In String: \\a"""
        self.assertTrue(TestLexer.test(input, expect, 194))


    def test195(self):
        input=""" "A random string with newline char \n" """
        expect="""Unclosed String: A random string with newline char """
        self.assertTrue(TestLexer.test(input, expect, 195))


    def test196(self):
        input="""abc 12_83.721e+128 "aslckas\\"\\"" xyz?" """
        expect="""abc,1283.721e+128,aslckas\\"\\",xyz,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 196))


    def test197(self):
        input="""not<2+5.2e-10>=abc and>=div<=-boolean"""
        expect="""not,<,2,+,5.2e-10,>=,abc,and,>=,div,<=,-,boolean,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))


    def test198(self):
        input="""0h90HL function 8DFe(Ph} inherit ZJD)tj12.45e-10i$KZWS4P&*5#9bf}I"V=iU8-iVQ^"""
        expect="""0,h90HL,function,8,DFe,(,Ph,},inherit,ZJD,),tj12,.45e-10,i,Error Token $"""
        self.assertTrue(TestLexer.test(input, expect, 198))


    def test199(self):
        input="""1e-10 % 2186481 = { 1, 5, 6} a : float ="ajksc^#!@\\n" """
        expect="""1e-10,%,2186481,=,{,1,,,5,,,6,},a,:,float,=,ajksc^#!@\\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))


    def test200(self):
        input="""Final Test Case: void = {"Nothing Here to say"??}"""
        expect="""Final,Test,Case,:,void,=,{,Nothing Here to say,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 200))