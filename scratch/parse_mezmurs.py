import re
import os
import json

raw_text = r"""Maqaa Abbaa Kan Ilmaa afuura Qulqulluu Waaqa Tokkotti Ni
                                              Amanna Ameen!!!
Faaruu Ayyaana CuuphaaSababeeffachun Karaa Kutaa 
Barattota Dilbataa M/A/Q/Mikaa`eel Qindaa`e.

Hub:-Jaalatamtoota fi kabajamtoota maatiwwan kiristoos kantaatan hundumti keessan nageenyi waaqayyoo isiinif haa bay`aatu baga har`a geessan.
Faaruuwwan barreeffama kana irratti argaman karaa kutaa faaruu barattota dilbataaM/A/Q/Mikaa`eel ayyana cuuphaa sababeefachuun kan qindaa`e yoo ta`u, Yeedaloo isaani barbaaduun akka qo`attan akkasumas dogoggora qubee fi jechaa uumameef nu ofkalchaa isinin jechaa bakka sirreffama barbaadutti sirreessun kan danda`amu ta`u gamanuman isin hubachiisuu barbanna!!!
Kutaa Faaruu M/A/Q/Mikaa`eel irraa.

Yaada fi Gaaffii yoo qabaattan bilbila kanaa gad jiru irratti bilbiluun ni dandeessu!!
Firaol Dabalaa 0919804735/0940045995.
                                             Baafata

1.Argadheen Jira!!!
2.Dubaraa Keessaa!!!
3.Malumaa!!!
4.Nageenya Keenyaa!!!
5.Aniif Mannii Koo!!!
6.Mucaa Kee Baattaadhutii!!!
7.Mooraa Loonii !!!
8.Gaalateeffamaadhaa!!!
9.Waa’ee Keen Hima!!!
10.Horee Iyeesuus!!!
11.Iyeesuus KiristoWaaqayyoodhaa!!!
12.Uifinnii Kee!!!
13.Kan Faayyuu Barbaduu!!!
14.Eegaa Hin Sodattinaa!!!
15.Jaalatamaadhaa!!!
16.Gaarummaan Kee Addaa!!!
17.Galmee Tsiyoon
18.Gaarii Kan Godhan!!!
19.Ni Dubbate!!!
20.Du’ee Du’a Koo Kan Hambisee!!!
21.Nan Himaa Gochaa Kee Goofta!!!
22.Yoordaanosittii!!!
23.Nu Fayyisuudhaaf Kan Dhalatee!!!
24.Gammanneerraa!!!
25.Umurii Koo Naaf Eebbisii!!!
26.Ni Galateeffannaa!!!
27.Mootich Yihuudaa!!!
28.Ammaa Ifatuu Nuuf Bahee !!!
29.Haadhummaa Keen Himaa !!!
30.Ofumaaf Mitii !!!
31.Maariyaam Ni Caaltii!!!
32.Aduu Caala!!!
33.Mikaa’el Naaf Dhufe !!!
34.Gammadika!!!
35.Maqaan Kee Natti Midhayee !!!
36.Gooftaa Siif Galataa !!!
37.Dhugumaa Dhugumaa !!!
38.Yaa Waaqayyo Gooftaa !!!
39.Koottu Haadha Koo !!!
40.Galatan  Galchaaf !!!
41.Mootichi  Yihudaa !!!
42.Ija Keenya !!!
43.Amantaan Tokuma !!!
44.Siif Haa Ta’u  Nagaanii!
45.Hore Iyyeesuus !!!
46.Tenagera
47.Inda Igziabiher Yale !!!
48.Kibra Kidusan !!!
49.Ba Midrawi Hiwot !!!
50.Mayidera Melekot !!!
51.Si Galateeffanna !!!
52.Jaalalan Hunda Goote !!!
53.Jajjabaadhaa !!!
54.Iyyeerusaalem Galuuf !!!
55.Galata Waaqayyoo !!!
56.Yeroo Isin Dhuftan !!!
57.Waa’ee Keen Hima !!!
58.Yaa Waaqayyoo Gooftaa !!!
59.Sidha Mikaa’eel !!!
60.Dubara Keessaa Filatamtee !!!
61.Mucaa Kee Baattadhuu !!!
62.Yohanisin !!!
63.Iliil Iliil !!!
64.Bu’uura Yeedaloo !!!
65.Ba Fikir Tasibo !!!
66.Tsinu Semay !!!
67.Qaanaa Zagalila!!!
68.Yalante Lane !!!
69.Ye Fikir Inat !!!
70.Sealilana !!!
71.Mariam Biye !!!
72.Anti Zaba Aman !!!
73.Nana Wada Igna !!!
74.Aduu Caala Ifa !!!
75.Kunoo Boji’amee !!!
76.Araarsummaa Isaanii !!!
77.Tsilat Ze Muse !!!
78.Arjummaan Isaa !!!
79.Hamalmala Worki!!!
80.Yiberral Ba Kinfu !!!
81.Taweidenaho !!!
82.Waan Inni Dubbate !!!
83.Miidhamuu Keenya Caala
84.Galatan Dhiyessaa !!!
85.Jireenyaa Lafarra !!!
86.Ulfinaa Waqaayyoo !!!
87.Kalleessaa Na Cesistee !!!
88.Jarreen Sun !!!
89.Maqaan Kee Ajayibaa !!!
90.Fooliin Kee Urga’aa !!!
91.Koottuu !!!
92.Sif Haa Ta’uu Nagaani !!!
93.Haadha Lubbuu Keenya !!!
94.Maariyaamii !!!
95.Waa’ee Keen Hima !!!
96.Du’aa Keessaa Nuu Bastee !!!
97.Maal Nama Godhe !!!
98.Iyyadege !!!
99.Kiristos Tewelede
100.Beheda Yohanis !!!
101.Hadigo Tesa !!!
102.Kinef Rigbi !!!
103.Bemennu !!!
104.Mariam !!!
105.Aklile Tsige !!!
106.Meaza Senaye !!!
107.Keme Tiberikene !!!
108.Yaa Waaqayyoo!!!
109.Nu Jajjabeessi!!!
110.Yoo Fayyuu Barbaaddee!!!
111.Dhisi Dhiisi !!!
112.Misle Mikael Wa Gabriel
113.Inza Tahakifiyo !!!
114.Yaa Waaqayyoo !!!
115.Du’a Keessa Nu Baastee !!!
116.Duraanis Kan Turtee !!!
117.Ijoollee Sadan !!!
118.Akka Iyyoob !!!
119.Sillese Weredu !!!
120.Serawit !!!
121.Ba Qana !!!
122.Kirkos Iyeluta !!!
123.Andebetem Yewuta !!!
124.Bakaranio !!!
125.Elshadayi Maqaan Kee !!!
126.Ye Kidan Tsilat !!!
127.Isey Silete Semere !!!
128.Yaa Gara  Laafeetti !!!
129.Du’a Fannoosatin Ajjesee !!!
130.Dhuguma Dhugaadha !!!
131.Samirraa Ni Bu’ee !!!
132.Urjii Dhan Dhufanii !!!
133.Qalbii Haa Jijjiirrannu !!!
134.Jecha Kee Dhagahuuf !!!
135.Seenaa Koo Haaressii !!!
136.Hin Callisinaa !!!
137.Zeweyineh!!!
138.Araarsituu Maariyaamii
139.Dursii Gooftaa Duraa Koo!!!
140.Namootaa Haa Gammannu!!!
141.Haadhaa Waaqa Kan Madaanalamii
142.Ishoo Gooftaan Nuuf Dhalate
143.Akkaa Daawiitii
144.Gugee koo
145.Ergaamon samii
146.Alfaafi omeegaa
147.Dhaadanoon koo siyii
148.Rajjii ulfiin kee
149.Egnaa inzemiralen
150.Nii cuphaame
151.Dhufeeraa mana kee
152.Waqayyoo adduunya dawatee
153.Ol bateeti
154.Cherneetu 
155.Galataa kee 
156.Haa galateefanu
157.Jabbaa mottii nagenyaa
158.Kottaa yaa namotaa
159.Iyyeesuus kiristoos
160.Naa jaabeserra
161.Turee fakkatuus
162.Ati yaa hadhaa dhugaa
163.Ol naa qabdee
164.Tallaq honewal
165. Handarri naaga
166. Haberetagn fikir
167. Metichalewu 
168. Yegna new 
169. Qulqulluu Mika’eel
170. Hoo Amalajitu
171.Simesh selam
172.Iyyasuus ati abbaa keenyaa
173. Jaalalaan hundaa gootee
174. Sittaan dhisee

        
1.ARGADHEEN JIRA!!!
Argaadheen jiraa dandii isaa dhugaa argadheenjiraa                                       Naan dogongorsuu baay’inni karaa isaa dhugaa irraa
Duris kan turtee hara’as kan jirtuu
Borus jirattee dhugaaf kan turtuu
Dhigaa waqayyoon kan hundefamtee
Aduunyaa guutuu irrattis kan hundefamte
Dhalloonni baay’een karaa jallissuu
Dhugaa dhisaanii mormii bay’isuu
Ilmaan waaqayyoo addaan qoodanii
Aangoo argachuuf dhugaa dabsani
Mee haa gaafannuu wangeela keenyaa
Isatu nuti himaa dandii ganamaa
Gototaa amantii mee haa gafannuu
Karaatti deebinee fayyina arganuu

2.DUBARAA KEESSAA!!!
Dubaraa keessaa filatamtee
Kennaa Waaqayyoo kan argattee
Gammadii yeeroo hundumaa (x2)
Yaa Mariyamii yaa giftiikoo abdin keenyaa sumaa

3.MALUMAA!!!
Malumaa maalin fakkeesinaaHadhaa gooftaa keenyaa(x2)
Giftii keenyaa qulqulleetti hadhaa keenyaa
Eyyeen Maryaamii maalin fakkessinaa

4.NAGEENYA KEENYAA!!!
Nageenya keenyaa waaqni keenyaa nageenya keenyaa
Jequmsa kaasee nuu yaaddeesus diinni keenyaa
Nutoo hin rafamnuu gooftaa qabna nageenya keenya
Diinni mo’amee humna gooftaan
Irraa ejannerraa fannoo isaan
Galmeen si’ooli digaamee
Misrachoo guddaan lallabamee(x2)
Nuu waliin jiraa baane galluu
Mootiin moototaa faajiin nagaa
Nuun dursuu karaa kamiini
Humna uffannerraa gooftanii(x2)
Yeemmuu innii ka’uu waaqni keenyaa
Duraa hin dhabbatuu dinni keenyaa
Humna Fari’oon rukutee
Gammachuun afaan nuu guutee(x2)
Rakkoon marfamee daandiin keenyaa
Baay’ee cimuu illee lollii keenyaa
Gooftaan dabarsee arginee
Waaqaa keenyaattis gammannee(x2)

5.ANIIF MANNII KOO!!!
Aniif mannii koowaaqayyoon waaqessina
Isatti amannee abdii godhaannee
Gochaa isaa dhugaa baanaa
Waarrii amalikoo naannoo keenyaa marsuu
Inni isaaniin oolchuu eessa jiraa jechuun
Goota beekamaadha innii waaqni keenyaa
Salphinaan deebisee waarra dinaa keenyaa
Isatti hirkannee humnii keenyaa hin laafnee
Gargaarsa isaatiin waanta heedduu darbinee
Maqaasa jajachuun nuyiif hojii keenyaa
Yoomuu hin irraanfannu oolmaa waaqa keenyaa
Akkaa Mariyaami obbolleetti Musee
Waaqayyoof hojjannaa isaa nu gaggeesse
Isarraan kan hafee kan biraa hin beeknu
Waaqa hormootatiif harkaa keenyaa hin laannuu
Naasuudhaan baqatee diinni sagaleesaa
Yemmuu dhaga’amuu saamii qaqawwessaa
Isaan sun humnaafi qabeenyaa isaaniini
Nut garuu ni moonaa yoomiyyuu taanaani

6.MUCAA KEE BAATTAADHUTII!!!
Mucaa kee baattaadhuti yaa hadhaa gooftaa
Kottuu mariyaamii(x2)
Kottuu(3)mariyaamii(x2) Eyyeen

7. MOORAA LOONII !!!
Mooraa loonii keessaa(x2)
Mooraa keessaatti dhalatee Amanu’eel(x2)
8.  GAALATEEFFAMAADHAA!!!
Galateeffamaadhaa ammaa baraa baraatti
Ammaa baraa baraatti mootiidhaa atii(x2)
Hundaa duraa akkaa jirtuu lafaaf samii
Haa dubbaatuu
Hundii darbees ni jiraatta yaa waaqakoo sif galataa
Baran hin daanga’uu ulfinniif Aangoon kee
Ililleen sii faarsaa dhaabbadhee fuulaakee
Warrii kaleessa mootii turan darbaniiru hardhaa hin jiraanii
Beektonniif ogeessonnii liqinfamaan du’aani
Dhaloonnii dhaalootaa barrii yoo darbuu baraan
Atii ni jirattaa mootii baraa baraa
Ergamoonnii samirrattii nifarfatuu maqaakeeti
Ilmaan namaa jilbeeffannaan sii waaqeessuuSif bitamuu
Dureessa hiyyoomsitee beella’a quubsita
Addunyaa kanarraatti enyuut sin qixxaata
9.WAA’EE KEEN Hima!!!
Waa’ee keen hima gochaa keen hima garummaa keen hima(x2)
Yaa iyesuus isaa jalatamaa
Amanu’eel fayyisaa ilmaan namaa(x2)

10.HOREE IYEESUUS!!!
Horee Iyeesuus(x2)
Him Geelilaa (x2) habe Yordanosi
Deemee Iyeesuus(x2)
Eyyeen Galilaa irraa garaa Yordanosii(x2)
11.Iyeesus kiristoos 
Iyeesuus kiristoos Waaqayyoodhaa jettee
Tawaahidoon waangeelan nu barsiisaa turte
Nutis dhugaa baana eeyyeen(x3)waaqayyoodhaa
Barumsii tewaahidoo kunoo kanadhaa
     Dinnii maaf gungumaa saammuudhaan dhibame
     Nutoo kan lallabnuu isaa fannifame
     Duubatti hin deebinuu fulduraatti mal
     Waaqa biraa hin qabnuu waaqayyoon si malee
Shakkii shakkitoota waan tokkoo hin raafamnuu
Tewaayidoon dhugadhaa tewaayidoo hin gadhisnuu
wangeelan  ijaaramee hundeen bu’uurrisaa
qilleensaa isa kamtu mana keenyaa raasa
  waa’ee qulqullootaas maaf dubbachuu dhiisna
  jireenyaa isaaniitiin gooftaa ittiin lallabnaa
 dhugaatu nuuf galeeraa duubattii hin deebinu
 dhugaadhaaf hojaanna namnii hundumtu haa baruu

12.UIFINNII KEE!!!
Ulfinnii kee kennaan kee jabaa
Simboo keetuu harkaanuu qaba
Mootichaa abbaa amantii
Taklayimmaanot nuuf koottuu ati
Biyyaa lafarraattii  kan adda baatee
Waaqayyoo keetii kan kaadhimamte
Biyyaa keenyaaf atii hardhaas kennadhaa
Ajaa’ibaa keetuu nuuf ragadhaa
Kaadhannaa keetii hara’a geenyeerra
Barumsaa amantas sirraa barreerraa
Inni ati nuuf kadhate waaqa biraa
Hara’as nuu eega nuu faana jiraa
Nutis jabaannee akkaa dhaabbanuuf
Amantii guutuun akkaa jiraannuuf
Harkaa keenya nuuf qabii abbaa keenyaa
Siin si ilaallee jabaannee teenya
13.KAN FAAYYUU BARBADUU!!!
Kan fayyuu barbaduu amantiif cuuphaadha
Eeyyeen dhugadhaa
Dhiigaan kan nuu bitee kiristoos qofadhaa
Eyyeen dhugadhaa	eyyeenggg
Sanyii namaa hundaafsami irraa gadii bute
Eyyeen dhugadha
Duutee du’aa moote jireenyaa nuuf lattee
Gooftaan sumadha
Harkaa Yohanniisittii yoo cuuphamtee ati
Eeyyeen dhugadha
Fakkeenyii kee hunduu maddaa jaalalattii
Fayyisaadha ati
Yoohannis yoo cuuphees bishaan dhaan inni
Eeyyeen dhugaadha
Kan nabooddeen dhufus ni cuupha abidaani
Inni hafuuraan
Lubbuu bade ture fayyinattii  baaafte
Eeyyeen dhuugadha
Waaqummaa keetiin jireenyaa nuu laatee
Du’aa nu oolchitee
Xaalayaa garbuummaa yordanosin ture
Eeyyeen dhugadhaa
xoofoo du’aa kootii jireenyaa jijjiiree
Du’aa nuu furee
Fayyinni amanta cuuphaadhan argamee
Eeyyeen dhugaadha
Addunyaa hundumtu isaan baraarama
Gooftaan furamaa
Fakkenyaa gugeetiin ni bu’ee afuurrii
Eeyyeen dhugaadha
Garaa keenya dhufee gooftaaan jaalalanii-----
Isaa bara ani
Fakkeessuudhaaf malee addunyaan sobaadhaa
Eeyyeen dhugaadha
Abbaan qulqulludha Amaanu’eel qofaadha
Inni gooftaadha
14.EEGAA HIN SODATTINAA!!!
Egaa hin sodatinaa(x2) gooftaatti amanaa
Galanaa Eektiraa          hin sodattinaa
Gooftaan nii baqaqsaa      >>
Waaqanii ni faayyisaa       >>
Kan keenyatuu caalaa       >>
Dheekamsa diinootaa       >>
Hirree gooftaa ilalaa         >>
Ilaala irreen waaqayyoo kuma kuffisa rukkuutee
Shootallii qaramuus       hin sodattinaa
Dinnii yoo burraqees        >>
Waranaa seexanaa           >>
Gooftaan nii dachasaa      >>
Yeroo dhumaaf malee      >>
Injifaamuun keenyaa hin   >>
Bakkeettii nuu hin dhissuu    >>
Guddaadhaa abbaan keenyaa  >>
Gooliyaadii heedduu utaalluus adda rukutaa iyyesuus
Dararamaaf cuubbu         hin sodattinaa
Waaqni nii dabarsaa          >>
Dhiyyee too hin haafuu     >>
Innii hin barisiisaa               >>
Barootaa dhiphinaa            >>
Gooftaa nii dabarsaa           >>
Yommuu hin digammuu galmii isaa utuunuti jiruu ilmaansaa
15.JAALATAMAADHAA!!!
Jaalatamaadhaa maaqaan kee
Eyyee hin argamnee kan akkaa kee
Fayyisaa lubbuu koo           Eeyyee
Si du’aa naa olcheee                 >>
Jalaqabaaf dhuumaa koo
Situu anaaf tolchee 
Afurrii dhalaa namaa               Eeyyee                                   Abdiichaa jaalalaa                   >>
Kan sittii amanee                    >>                          
Du’uu jalaa gala                     >>
Jaalalaan beekamtaa             Eyyee
Hundumaa biraattii                  >>
Anii siin barreffadhaa              >>
Onnee koo irrattii                     >>
Galaanii haa callisuu                  Eeyyee
Siin jedhuu iyyesuusii                    >>
Naaf atoo mo’aadha                      >>
Si wamuun kiristoos                      >>
Haa baadhadhuu maqaan kee     Eeyyee
Innii hundaa caalluu                      >>
Adduunyaan kun martuu              >>
Ajajaa keen buluu                         >>
Maqaa fayyinatiin                         Eeyyee
Hundaaf kan latamtee                     >>
Takkaa bade hin hafuu                    >>
Kan sitti amanee                              >>
Duuti du’unni hafee                   Eeyyee
Bilisaa nuu baaftee                         >>
Mallattoo fayyinaa                         >>
Dhiigaa kee nuuf lattee                  >>
16.GAARUMMAAN  KEEADDAA!
Gaarummaan kee addaa garraamummaashesi (x2)
Haadhasaa taatettaa qorichaa addunyaafi
Qulleettii wan taateefhaadhaa haadhaakeenyaa(x2)
Mudaa kan hin qabnee                   >>
Gooftaa nuuf deessetta                  >>
Kan sirraa dhalatee              >>
Seenaanshee raajiidhaa haadha keenyaa(x2)
Duumessaa dhugaati                 >>
Gammachuun hundumaa          >>
Abdi tewaahidoo                      >>
Eegduu jennataati      haadhaa keenyaa(x2)
Gonfoonsheerra bulee              >>
Yaabbannoo samiiti                 >>
Abdii tewaahidoo                    >>
Seenaan kee raajiidha haadhaa keenyaa(x2)
Abidaa abbaati                           >>
Duumessaa dhugaatii                 >>
Abdii hundumaatii                     >>

17.  GALMEE TSIYOON
Galmee tsiyoon faaruun guutamtee                                                                        Ulfinaa durboof iliil jedhaamee
Akka biiftuudha kan iftuudha(x2)
Olleerra ishee faarfaachuudhan
   Humna kan naaf kennuu mi’aa maqaa ishee
   Meeshaa galataa ishee fudhannee ilillii ishee
   Chaappaan eebbasheetii keessaa keenya jira
   Maariyaam yemmuun jedhuu rakkoon koo darbee
Galannii ogummaa qabeenyaan galataa
Mana isheetti dhufnee argineerra tola
Baanerraa iddoo gadiiti ishee abanneeti
Tsiyoonirra faarfannaa isheetti marsuuni
Gorsa ogeessotaan mul’attee dhoksaatti
Afaan daa’imaatiin mul’atte ifatti
Beeteliiheem dhageesse jecha misiraachoo
Jaalalan guutame buufanni waaqayyoo
Mootichi ilma ishee kiristoos wajjini
Akka tasaatti buunee tulluu du’aarraatii
Firii ishee dhamdhamna laphee jaabannerra
Kan sichii nagaadha hin arginu soda

18.GAARII KAN  GODHAN!!!
Gaarii Kan godhan dubartoonnii jiru
Obsaa guddaadhaan waaqa wajjiin turuu
Kan kee garuu isaan keessa addaa
Yaa maariyaam ulfinni kee guddaa(x2)
Kaasominaa fi gara laafummaa kee
Sirraa barannee nuti ijoollonnikee
Akkamittiin gochaa kee ibsinaa
Yoo mal jennee garaa si ciibsina
Barcumaa ulfina daksiiyoosiif laatte
Sareen dheeboonnaan ati bishaan obaaste
Namaa qofaaf mitii garaan kee kan nahu
Kan sijibbaan hunduu ni qana’uu
Barbaade hin arganne waaqni kan akkakee
Hin jijjiramne chaappaan durbumma kee
Dhaalota kan ta’ee hunduu sinaa faarsuu
Arjaa ta’uukee dhalootatti haa labsuu
Oolmaa kee yaadatee hunduu imimmaan roobsa
Gaarramummaan kee hunda keenya boonsaa
Galteeta hin baatu laphee keenya keessaa
Si wajjiin jiraachuun nuuyifoo bayeessaa
19.NI DUBBATE!!!
Ni dubbatee Izraan ni dubbatee
Daawwiit faarfaatee(2)
Ni dubbate dubbii waaqa isaa Daawwit faarfate
“      “    Waa’ee faayyisaan dhalachuu isaa
“       “   Beeteliheem gammadi Daawwit farf
“       “   Yaa biyya raajoota jechuun faarfate
“       “   Bagana rukutee Daawwit faarfate
“      “    Daandiin dukkana’ee ni ifa jedhee
Izraan ni dubbatee Daawwit faarfaate(4)
Ni dubbatee hawwiidhan guutame Daawwit faarfate
“    “      Afuuraan ilaalee ragaaf dhaabbatee
“    “      Namoota gammadaa Daawwit faarfate
“    “      Bultoo jecha Abbaa argachuuf hawwee
Ni dubbate kiristoos ni dhufa Daawwit faarfatee
“      “        Jaalalan waamame jechuun dubbate
Nan hima gochaa kee gooftaa yeroo hundumaa
Nan himanan himaa gochaa kee gooftaa
Afuura qulqulluu    Nan hima gooftaa
Bartootaaf kan buuste “     “       “
Gochaa kee dubbachuu      “      “      “
Ati na boojite                  “      “       “
Seenaa koo jijjiiruun          “       “       “
Situ na filate                     “       “       “
Argama jireenyaa       Nan hima gooftaa
Isat qaba beenyaa        “     “       “
Alfaadhaf omeegaa     “      “        “
Fayyisaa Addunyaa       “      “       “
Dhiiga loolasee            “      “      “
Isat nu fayyisee            “       “     “
Abbarraa dhalatee     Nan hima gooftaa
Samii gubbaarratti     “     “        “
Haadha irraa dhalatee   “     “        “
Biyyaa lafaa irraatti       “    “       “
Fayyina koof jettee        “     “       “
Gidiraa fudhattee          “     “       “
Yoohannisin waamtee       Nan hima gooftaa
Lafa onaa keessaa             “      “      “
Abbaa jaalaladha             “       “      “
Inni nu gargaaree            “       “       “
Barsiisaa dhugaadha      Nan hima gooftaa
Inni nuuf dhaabbatee      “     “     “
Abbaa koo jeedheraa        “     “      “
Baraa hanga baraatti         “     “      “


20.DU’EE DU’A KOO KAN HAMBISEE!!!
Du’ee du’a koo Kan hambisee nagaa naflabsee(x2)
Aarsaa Abirahaami  Eeyyeen Nuti ittin fayyinee
Jaalala waaqayyoo       “       Kan isaan arginee
Guyyaansa yoo gahu    “      durbeerra dhalatee
Fannoo irra kan oole     “     fayyina nuuf latee
    Fannooti ol bahee nuuf dhiphatee nu fayyifatee(2)
Akka uumamatti   Eeyyen  Gooftaan ilaalame
Dhiiga isaan na bite   “    Nagaan naaf labsame
Gidiraan Waaqa Koo “    Anatti mul’ata
Daandiin jireenya koo “   Isaan naaf mijata
  Ummanni hundumtuu si farfafata nuf deesse goftaa
Duran Kan yaadamte Eyyen yaada abba keessati
Haati Amaanu’eel      “   Naafis Haadha kooti
Ati miidhagina Koo    “   Yaa durbee Haadha ko
Akka jedhan miti   “   Naaf kadhuu gooftaaUumamni      hundumtuu si farfaataa nuuf deesse gooftaa(2)
Du’ee du’a koo kan hambisee nagaa naaf labsee(2)
Durbe maariyam qulqulleeti mi’oftuu yaa haadha mooti(2)
Uumamni hunduu si waamata waaqayyo situ kadhata
Mallattoodha biyya keenya taawahidoo amantaa dhugaa
Fuula waaqa ni dhaabbata gabri’eel nuuyif kadhata
Kan gargaarte Israa’eeli mikaa’eel kottu araarami
Kiristoosiif amanamtee arseemaan kunoo nuuf dhuftee
Lafa irratti kan dhalatee Yoohannis eenyu akkakee
Wareegama Giyoorgisii nuuf koottu maaloo har’asii
Kan kabaje qulqulloota ni argata gatii tolootaa
21.NAN HIMAA GOCHAA KEE GOOFTA!!!
Nan himaa gochaa kee gooftaa yeroo hundumaa
Nan himaa (x2) gochaa kee gooftaa(x2)
Daawwit kiraarani        Gochaa kee gooftaa
Izraan masiinqooni               >>>
Hunduu qulqulloonni            >>>
Maqaa kee faarsanii               >>>
Galaana addaan kuttaa        Gochaa kee gooftaa
Nyaata samii buustaa             >>>
Dukkana ibsitaa                     >>>
Diina injifattaa                       >>>
Lafa jabeessitee       Gochaa kee gooftaa
Humna kee kennitee             >>>
Golboo qajeelchitee              >>>
Naafa adeemsistee                >>>
Jaamaaf ija laattee              Gochaa kee gooftaa
Du’aa bol’aa kaasta                    >>>
Maraatu fayyista                         >>>
Seexana aryattaa                         >>>
Kan namni tuffatee       Gochaa kee gooftaa
Ati ulfinaa laattee                  >>>
Isa abdii kutattee                   >>>
Afuura kee laattee                  >>>
22.  YOORDAANOSITTII!!!
Yoordaanosittii nuuf cuuphameera (x2)
Abbaan ifaa baasee iccitti tokkumaa
Mucaan koo kunooti inni jaallatamaa
Addaamiin booj’ee kan cabsee garbummaa
Mucummaa cuuphaadhaan argannerraa(x3)
Seexanicha eyyeen moo’anneerraa(2)
Faaruudhaaf>>dhaabbanneeraa (2)
Halkaan dukkanaa’us gooftaan nu ga’eeraa
Irree keenyaa ta’ee nutis dhaabbanneraa
Cuuphaasan cuuphamnee diina moonee jiraa
Yordaanos (2) gammadikaa x(2)
Gammadikaa eyyee gaammadikaa
Mootichaa kee >>>simmadhuu kaa
Fiigichaa kee >>>raawwadhuun kaa
Gooftaa kee >>>faarfadhuu kaa
Seenaa kee haaromee dhaabbadhuu faarfadhuu
Teellaatti hin deebi’iin gooftaa kee simaadhuu
Maaqa iyyeesuusiin seenaa haarefadhuu
Cubbuu addaamiin duuneerraa
Cuuphaa gooftaatiin kaaneerraa (x2)
Du’aa injifannee kaanerraa
Waanjoon seexanaa cabeeraa
Yoordaanoos(2) kan carroomtee (x2)
Kan carroomtee  eyyeen kan cayyoomtee
Jaalalaa gooftaa kan >>> kan argattee
Raajii dawitiif  >>> kan raawwattee
Jechaa waaqaa >>> kan simattee
23.NU FAYYISUUDHAAF KAN DHALATEE!!!
Nu fayyisuudhaaf kan dhalatee amanu’eelidha(2)
Kan dhalattee amaanu’eelii (x4)
   Durbeerraa dhalatee nu fayyiseera kansaa tanerraa
   Nu fayyiseeraa kansaa taanneeraa  (x4)
Ati yaa seexana diina keenyaa nurraa fagadhuu
Diinaa keenyaa nurraa fagaadhuu  (x4)
Gooftaan jabeessee nuu dhabeera garaakutadhuu
Nu dhaabeeraa garaa kutadhuu  (x4)
Dhiigaan nu bitee nu holchateera harkaa diinarraa
Nu hoolchaateeraa harkaa diinarraa  (x4)
    Gooftaan barbaade nu waameera sirkaa baaneraa
    Nu wameerraa sirkaa baanerraa (x4)
Ergamaan mikaa’elaa nuf dhuufeera si mo’anneerraa
Nuuf dhuferraa si mo’annerraa   (x4)
Ergamaan garbi’eel abidarraa nu hoolchateeraa
Abiddaarraa nu holchateraa (x4)
24. GAMMANNEERRAA!!!
Gammanneerraa sirriittii gammanneerraa
Waaqayyoon eebbasaa nuuf keennerraa
Kunimee raajiidhaa     gammannerraa
Mee koottaa ilaala                >>>
Namoonnii hin faarfatuu      >>>
Akkummaa ergamoota         >>> 
Kaleessaas Kan turee              gammannerraa
Baraan Kan jiraatuu                     >>>
Mootii bara baraa                         >>>
Maqaan kee haa ulfaatu               >>>
Fannoo kee yoo arguu      gammannerraa
Garaa naa haammaata         >>>
Anaaf dhiphachuu kee        >>>
Laphee naa yaadataa           >>>
Xaalayaa yakka koo      gammannerraa
Tarsaasuuf jettee                >>>
Tabbaa qaraniyoo               >>>
Fannoorraa naaf ooltee       >>>
Obbolloonnii ilichaa          gammannerraa
Waaqa guddaa faarfadhaa               >>>
Waanti isaaf galchinuu                    >>>
Galataa duwwaadha        >>>
Kan dhifamaa hin qabnee      gammannerraa
Harkaa diinaa keessaa               >>>
Kan jalaa nuu bassee                 >>>
Waaqayyoo eebbisee                 >>>
25.UMURII KOO NAAF EEBBISII!!!
Umurii koo naaf eebbisii bara gaabbii koo
Kan diina koo akka hin taane galgalli kan koo
An harka keerra jiraadhee du’uu naaf wayya
Xummura koo naaf miidhaksii maaloo uuma kiyyaa
Mukti baala baasee fagoo irratti mul’atu
Gogee too ni bada hoongee hin dandamatu
Naf hin kenniin gooftaa umurii gaabaabduu
Yeroo dhaaf mul’atee booddee kan dhokatu
Nan taasisini biqiltuu hin guddannee
Nan taasisini muka firii hin laannee
Na godhadhuu malee nama siin jiraatuu
Caamsaan yoo dheeratees isa dandamatuu
Daraaran miidhagdee bakka hundati mul’atu
Yeroo yartun booda wayyaa gaddaa uffattuu
Miidhaginni toole kan umurii hin qabnee
Nan taasisin maaloo kan siin hin jiraannee
Sibiillii miidhagdee warqee kan fakkaattuu
Abidda osoo seente tasa keessa hin baatu
Lakkii warqee mitii innoo maadaabiidha
Margii mimmiidhagduus jallishee dhoqqeedha
Akka karaatti hafee Deemaas manaa bahee
Miidhaginni Addunyaa qalbii isa booji’ee
Biqiltuun biqiltee qoree keessa buutee
Akka hin guddanneef hudheetu qabatee
26.NI GALATEEFFANNAA!!!
Ni galateeffanna waaqayyoo abbaa keenyaa
Ni galateeffanna
Ni galateeffanna waaqayyoo abbaa keenya
hundumtikeenya
Beeteliyeem keessatti waaqni nuuf dhalatee
Harka diinaa keessaa gooftaaan nu baafate
Ililleeen faarfadha ijoolleen Addaam
Kunoo nuuf dhalatee waaqayyoo guddanii
Mooraa loonii keessa galma isaa godhatee
Obsaa fi kabaja gooftaaan nu barsiisee
Araarri nuuf bu’ee dhalachuu gooftaani
Namnii fi ergamoonni waliin faarfatanii
Raajiin gooftaa keenyaa yoom kana raawwate
Yoordanoos keessatti cuuphamuun raawwate
Abbaa ilma afuura qulqulluu
Yeroo cuuphamanii of ibsaaniiruu
Abbaan kiristoosi samirraa gad bu’ee
Kan narraa dhalate ilma kooti jedhee
Waan ilmi koo jedhee hundasaa raawwadhaa
Jedhee nuuf ibseera umaan samiif lafaa
Xalayaan garbummaa baraaf kan dhokatee
Cuphaamuu gooftaatiin battala tarsa’ee
Yaa ilman namootaa gammadaa ililchaa
Gooftaan diina moo’eee galata isaaf galchaa
27. MOOTICH YIHUUDAA!!!
Mootichi yihuudaa Iyyeesuus gooftaadha(x2)
Anisnan jedha Waaqa koo Iyyeesus seeni mana koo(x2)
Giifti koo misirroo Soolomoon siin jedhee
Anis nan jedha Haadha koo Maariyaam seeni mana koo(x2)
Angafti ergaamoota Mikaa’el sumadha
Anis nan jedhaam eega koo Mikaa’eel seeni mana koo(2)
Ijoollee sadaanii abiddaa kan baastee
Anis nan jedhaam eega koo Gabri’eel seeni mana koo(2)
Mootichi amantii Takliyyee sumadha
Anis nan jedhaa abbaa koo taakliyyee seeni mana koo(2)
Mootichi Ziqu’aalaa Abuhee sumadhaa
Anis nan jedhaa abbaa koo Abuhee seeni mana koo(2)
koottu duumessani(x4)
Fayyisaa keenyaa       Aaraara keetiin
Durbee maariyaam kadhanna keetin
Ergama Mikaa’el eegumsa keetiin
Ergama Gabrii’eel       eegumsa keetiin
Ergama Ruufa’eel        eegumsa keetiin
Ergama Uraa’eel         eegumsa keetiin
Ergama Raagu’eel       eegumsa keetiin
Ergama Faanu’eel       eegumsa keetiin
28.AMMAA IFATUU NUUF BAHEE 
Ammaa ifatuu nuuf bahee(x2)
durbeerraa dhalatee fayyinaa nuu ta’ee
Samiirraa gad bu’ee addaamin barbaadee(2)
Taayita isa jalqaba deebisuudhaaf jedhee
lubbuu isherraa lubbuu foonsherraa hirmatee(2)
Fanniifamuu isaatiin du’aa nuu oolfatee
dureessas yoo ta’uu kan danda’uu hundumaa
beela’ee dheebotee baatee ba’aa namaa
Aakkaa barbadaa’uuf ogummaan seexanaa
Foon addaam uffatee nuuf ta’ee fayyinaa
29.HAADHUMMAA KEEN HIMAA !!!
Haadhummaa keen himaa ya haadhaa koo (x2)
Yaa faakkaattuu gugee garraamii koo
Abjuu koo dagadhee dhugarraa hin ijaajjuu
Kan koo kan hin taannee sobnii nan ajajuu
Dhugaan sirraa argamee jaalala kandeessee
Maariyaam sin waamaa maqaa kee ol kaasee
Jireenyaa isa laatuu barruukeerraati baattee
Ilmaa kee iyyeesuus duukaa kan godaantee
Keessii koo amanee waa’ee keen nii faarsaa
Anis dhalootadha sichaan si leellisaa
Akkaa abbaa efreem galataa keen himaa
Jaalala keef durbee anaa nan warreegamaa
Oduu diinaa ilaalee boodattii hin deebi’uu
Tokkichaa jedheera sirraa addaa hin ba’uu
30.  OFUMAAF MITII !!!
Ofumaaf miti nuu waamuun kee
Samii samirraa gadii bu’uun kee
Bilisaa nuu baaseeraa humnii kee
Nurraa golboobeera ayyaannii kee
Ofumaaf mitii nu waamun keeIddoo isaa garii        qophessitee
>>              Waanta nuuf ta’uu murteesitee
>>              Boddee hin deebinuu murtoofnerraa
>>               Arjaa ta’uu kees hubanneerraa
Ofumaaf mitii nu waamun kee Furmannii keenyaa wallalamee
>>                 Nama birrattis tuffatatamnee
>>                 Galmeen keenyaa siin haarrefamee
>>                 Misiraachoo guddaan lallabamee
Ofumaaf mitii nu waamun ke Adeemsaa keenyaa nuf sirreessii
>>                 Galaana cubbuu nuu ceesisii
>>                 Simallee kan nuuf ta’uu hin jiruu
>>                 Arjaan akkaa keetasaa hin jiru 
Ofumaaf mitii nu waamun ke  Iddoo nu waamtee hin irraafannu
>>               Maqaa kee waammachuu hin nufinnu
>>               Mucummaatti nu guddifattee
>>               Bakkaa honaatii nuu waammattee
31. MAARIYAAM NI CAALTII!!!
Maariyaam ni caaltii uumamaa hundarraa x2
Ishee hin gubnee abiddi waaqummaasa x2
Midhagduu akka warqee urgoftuu gannataa
Kabaja keef jecha jilbi koo hoollataa
Simannaan kee addaa koottumee haadha ko
Ifa keetiin guutii bososaa godookoo
Lafa honaa keessaa godaanuu keen argee
Ati qoricha keenyaa haamileen koo margee
Ati madda boqonnaa deessee naan badhaastee
Kanaaf human gadii uumamaan ol taatee
Karra ishee cufamtuu karaa bahaan argee
Isqeel dhugaa bahaa durboo ulfina kee
Tasa sirraa hin maqnee hundumaa argeeraa
Nan dhabiin hayyoo koo ati waltajjii keerraa
Dirree qabsoorrattii ilma keetiin bahee
Injifadheen galee diinni koo hin qaana’ee
Hundeen kee hin jiguu Qabata abboota koo
Maariyaam x2 jedhee hin quufuu arrabni koo
32. ADUU CAALA!!!
Aduu caala ifaa fuulli isaa eeyyen x2
Nagaadhaan galanii biyya isaaniitti x2
Qulqulloonni gooftaa warren amananii
Dhugaa dubbii isaatiif hundumaa dhiisanii
Jiruu biyya lafaa hundumaa dhiisanii
Addunyaa hadhaa’e wangeelaan jiisanii
Fedhii biyya lafaa hundumaa dhiisanii
Maqaa iyyesuus addunyaaf labsan
Abidda boba’u keessa dhabbatanii
Maqaa maqaa caalu kanaaf argatan
Dhagaan dhaa’aman dhugaa lallabanii
Mana hidhaa keessatti raajii hojjatan
Isxifaanos fa’aa biyyicha galanii
Gonfoo isa ulfinaa kanaaf argatan
33.MIKAA’EL NAAF DHUFE !!!
Mikaa’el naaf dhufee gadduun koo hin hafee
Naannoo kan koo(x3)buufate nagaan koo eeyyen
Angafni ergamootaa tajaajilaan gooftaa
Mo’annaan dhaabbatee mo’atee diinotaa
Gartuu isaa waliin iriiratti duulee
Gareen saaxinaa’el si’oolitti gatee
Gabreel naaf dhufee diinni koo ni kufee x2
Jijjiiramee( x3)duuti koo labsamee eeyyen x2
Karoora diinotaa karaatti ambisee
waaqarraa ergamee abiddichas dhaamsee
naabukadanatsoor mootii baabiloon
kaayyoon isaa diigamee maqaa gabreeliitiin
dhufee rufaa’eliin raamaa irra ariitiin
dhiphina koo (x3) furuudhaaf rakkoo koo
dhukkuboota amoorraa nama akka fayyisuuf
gadameessa haadholiis nagaan akka hiikuuf
aboon kennameeraaf waaqayyo biraatii
qulqulluu rufaa’el nuuf koottu ati har’as
Waaqayyoon qulqulluu warren sodaatanii
ni fayyisuu(x3) ni ergamoonnii 	GA	]				 mn
34.GAMMADIKA!!!
Gammadikaa( x2) yaa maariyaam gammadikaa
Karaa keen dhufee    Gammadikaa
Gabreelii ergamaa                >>
Gammadi jedhee               
Si galateeffatee                  >>
Jedhe ayyaana qabeettii       >>
Durbee qulqulleettii              >>
Qaana galiilaattii           Gammadikaa    
Mana cidhaattii                    >>
Dookimaas dhiphatee          >>
Wayiniin dhumatee              >>
Guuttee dinqaasaa               >>
Laattee hir’ina isaa               >>
Si jaalannaa (x2) maariyaam si jaalannaa
Si jaalannaa (x2) haadha keenyaa si jaalannaa
Sanyii nuuf haftee                >>
Fayyinaaf taatee          >>
Otoo ati hin jirree         >>
Nu banneet turree         >>
Kanaaf si jaalannaa       >>
Nuuf deesse atii       Si jaalannaa
Waaqa waaqotaa              >>
Beetileemittii                    >>
Mootii moototaa               >>
Kanaaf si waammannee    >>
Maariyaam siin jennee      >>
Nuf kadhadhu( x2) maariyaam nuuf kadhadhuu
Nuuf kadhadhuu (x2) kiristoos nuuf kadhadhuu
Rakkina dookimaas            >>
Ati kan hubattee                 >>
Rakkannee har’aa               >>
Yeeyyiin nu seentee           >>
Haadha kadhannaa             >>
Maariyaam si waamna        >>
Nuuf kadhuu( x2) ilma kee nuuf kadhuu
Waadaa fayyinaa               >>
Guyyaa rakkinaa                >>
Nutoo si waammannaa       >>
Yeroo dhiphinaa                 >>
Si qabanneerraa                  >>
Haadha araaraa                   >>
Nan dagatiin gaafa murtii maariyaam qulqulleettii
Dhiphadheen jiraa            nan dagatiin
Hin qabu firaa                       >>
Sitti of kenneerraa                 >>
Waadaa araaraa                     >>
Haadha koo adaraa                >>
Murtii amaarraa                      >>
Qabadhee eebba kee     >>
Seeni mana koo             >>
Naa kadhu ilma kee      >>
Waa’ee cubbuu koo      >>
Maariyaam adaraa        >>
Murtii du’aarraa            >>
35. MAQAAN KEE NATTI MIDHAYEE!!!
Maqaan kee natti midhaayee afaan koo keessattii
Dammaaf walalaa caalaa akkamiin si dagadhaa
Yaa haadha jaalalaa
Si faarsee ani hin quufu tasa si dhiisee hin deemu
Laphee koorratti biqiltee jaalala haadhummaa keetii
Jireenya koo boojitee
Ati na dhunfattee kana booda ani kan keetii
Na guddistee kunuunsitee mana keettii
Maal akkamii barruu guddise irraanfatuu
Barruun soore harki obaase nama hin gaafatuu
Jechaatiif malee dammiif aannan si madaaluu
Laphee koo keessaa bakka qabdaa kan hunda caaluu
Kabaja keef jechaa jecha aaraa qindeeffadhee
Sin faarfadhaa ormoota dura dhaabbadhee
Ijoolleen ormaa mana nyaataa ala ilaaltii
Jechuun dubbatuu abbootiin keenya durattii
Kan kee miti malee si waliitiin turuu
Ormmummaadhaan si dhiisanii deemaniiruu
Lapheerraa mitii afaan qofaan si faarsanii
Garaa si atuun qarshiidhaan si jijjiiranii
Hin jijjiiru anoo kennaa fannoo jalaa
Si naaf kenne ilmi kee abbaan jaalalaa

36.GOOFTAA SIIF GALATAA 
Gooftaa siif galataa x2
Situ hundaa hojjataa
Dureessas                  eeyyen
Kan iyyoomsu              >>
Kan rakkate                  >>
Kan dureessu                >>
Dhukkubsataa               >>
Kan fayyisu                   >>
Ija jaamaa                      >>
Si kan ibsu                     >>
Matsaaguus                    >>
Kan fayyisuu                  >>
Ciisicha isaa                    >
Kan baachisee                 >>
Gooftaa kee raajiidhaa x2
Ani maalan jedhaa                         eeyyen
Fannoo keetiif               >>
Ni sagannaa                   >>
Cuuphaa keetti              >>
Ni amannaa                   >>
Armee keetis                 >>
Ni kabajnaa                   >>
Maqaa keettii                >>
ni amannaa                    >>
Iyyesuus sitti amannaa x2
Maqaa kees waammannaa
mootummaan kee         eyyeen
dhuma hin qabu               >>
kan siin bahee                  >>
homaa hin dhabu             >>
fayyisuu kee                    >>
argineerraa                      >>
fannoo keeyiin                >>
fayyineerraa                    >>
innufinuu                        >>
bonmaaf ganna               >>
nuti yoomiyyuu              >>
si faarfannaa                   >>
kunoo ilil jennaa (x2)
maqaa kee faarfannaa
osoo hin balleessine          eeyyen
fannoo baattee             >>
cubbuu addaam            >>
haquuf jettee                 >>
waaqa oolmaan kee       >>
naaf hedduudhaa          >>
waan hundumaa           >>
nan yaadadhaa               >
yemmuu namni             >>
gadi na dhiise                >>
gooftaa situ                   >>
ol na kaase                    >>
kee maaltu irraanfataa (x2)
Hundi ni yaadataa

37.  DHUGUMAA DHUGUMAA!!!
Dhuguma dhugumaa x4
Fayyisaa koo galata kee        x2
Maalan jedhaa jaalala kee
Cubbuu koo isa dhoksaa osoo ifa baastee
Haa hafu jettee osoo dhiisuu baattee
Natti osoo lakkooftee ammeenya garaa koo
Iddoo hin qabu baayy’eedha cubbuun koo
Daqiiqaa keessatti cubbuun ani hojjadhu
Ati balleessi yemmuun si irraanfadhuu
Ati garuu fuula kee nattii hin jijjiirreenee
Ulee dheekkamsa keen atisoo nan reebnee
Araara kee ergii har’a na fayyisii
Cubbamaa ta’uu koobeekaa mee dhiisii
Cubbuun na harkisaa biyyaa lafaa kunii
Jiraachuu hin dandeenye qulqullumaadhani
Gochaan biyya lafaa gaarii fakkaatuyyuu
Boodden isaa badiidhaa gonkumaa hin mi’aawuu
Ati nan deebisnee akka balleessaa kootti
Waanin jedhu hin qabu si haa gahu galanni koo

38. YAA WAAQAYYO GOOFTAA !!
Yaa waaqayyo gooftaa(x2) si galateeffannaa
Suma malee kan biraa maal qabnaa (x2)
Yaa maariyaam giiftii (x2) nutoo si jaalannaa
Waan nuu deesseef qoricha addunyaa
39.KOOTTU HAADHA KOO !!!
Koottu haadha Koo Maaramii
Maaloo nu jidduutti a.rgamii
haadha gooftaa yesuus kan amanu’eelii
Badiidhaaf bobbaanee yemmuu isa yakkinee (x2)
Gatii badii keenyaa isheen baraaramnee
Hir’inaaf dhiphina dookimaas hubattee
Leeyya’uu jalaatiis kunoo isa hoolfattee
Koottaa amanadhaa lapheedhaan cabaatii (x2)
Haadha dhugaa kanaa fudhaa qabadhaatii
Yakki koo baayy’atee yeroon dhiphadhetti
Harki maariyaam ol na qabatteetti
Gonfoo qulqullootaa haadha cubbamootaa (x2)
kunoo si waammannaa maaloo akkam nu gootaa
Egaa maariyaam nu yaadadhuu
Dhiifama ilma kee nuuf kadhadhu
Biyya kee kan taate Itiyoophiyaa yaadadhu
Tawaayidootti amannee akka dhaabbannuu
40.GALATAN GALCHAAF !!!
Galatan galchaafii waaqa kootiif
Bultoo isaa ol seenee sagadee isaafii
Haallee haalle-luuyyaa halle-luyyaa jedheen
Holmaasaan dubbaadha waninni naaf godhee
Jabaadha waaqayyoo hunda ni danda’aa
Jecha sagaleesaan hundumtuu ni ta’aa
Isaanan argadhee nagaa mana kootii
Haalfaadhaa omeegaa inni abdii kooti
Afaan leencaa cufee abiddas ni dhaamsee
Jiraataa nu godhee du’a keessaa nu baasee
Mootii samiif lafaa gooftaan maal dadhabaa
Qilleensa keessasoo innoo karaa qabaa
Bakkeetti gatamee miidhamee qaamni koo
Calliseetoo darbee na laalee firrii koo
Suphee ol na kaasee caba koo dhidhiibee
Galanni isaaf haa ta’u fuula isaa na dhaabee
Dhiiga isaa qulqulluun mallatteeffameeraa
Dame meetii qaphee galataaf ka’eeraa
Sagalee moo’ichaan nan waama maqaasaa
Bara jireenya koon dubbadha waa’ee isaa
41. MOOTICHI  YIHUDAA !!!
Mootichiyihudaa iyyeesus gooftaadhaa (x2)
Anisnan jedha waaqa koo iyyeesuus seeni manaa ko
Giiftii koo misirroo solomoon sin jedhee
nis nan jedhaa hadhaa koo maariyaam seenii
Manaa koo
Angafnii ergaamotaa mikaa’eel sumaadha
Anis nan jedham egaa koo mikaa’eel seenii mana koo
Ijoollee sadanii abidaa kan baastee
Anis nan jedhaam eegaa koo gabri’eel seeni
Mana koo
Mootichii amantii takliyyee sumadhaa
Anis nan jedhaa abbaa koo takliyyee seeni mana koo
Mootichi---------- abu’ee sumaadhaa
Anis nan jedhaa abbaa koo abu’ee seenii manaa Koo
Kottuu duumessaani( x4) faayyisa keenyaa araara keetiin
Koottuu duumessaani ( x4) ergamaa mikaa’el egumsaa
Keettiin
42. IJA KEENYA !!!
Ija keenya ati maayiyaami si nujala hin tuqiini
Ijoolleen tewaahidoo hin jaalamaa siinii
Seeni mana keenyaa atoo eebba keenyaa
Waaqayyoon waan deessaaf ati haadha keenya
Hirdhina namoota dursitee kan beektuu
Saalfii fuula nama kan namaf olchituu
Daadhiin dhumachuni dhiphatee Dookimasii
Ati kadhanaa keetiin guutafa daadhichaa
Akkaa abbaa hiyaaqosi si galateeffatee
Akkaa si faarfatuu lapheesa kan seentee
Waan taateef sababa ati fayyina keenyaa
Nuti si jaalannaa waaqa gooftaa keenyaa
Guyyaa jimaataayiin badhaasa keenya taatee
Fannoo jalattisoo ati kan nuuf kennamtee
Waadaa fannoo jalaa isa qaraaniyoorraa
Gooftaatu nuuf kennee jedhe haa keetoo
Daa’imummaa kaastee ati harka na qabdee
Akkan si faarsuufis kennaa keen na dibdee
Dhaloonni hundumtuu qulqulleettii jedhuu
Maqaa keen olkaasuu anis dhalootadhaa

43.AMANTAAN TOKUMA !!
Amantaan tokkumaa(x2)
Eeyyen (x2) gooftaan nuti amannu
Eeyyen innoo tokkumaa
Warri shakkitootaa afaan isaanii bananii
Amantaan keessano gooftaa hedduuf sagadii
Kan nuti amannu lakkii kana mitii ------------
Nuti kan waaqessinu ilma maariyaamitii
Cubbuu keenyaaf jecha samiirraa gadi buutee
Waaqummaa isaatiin foon namaa uffatee
Iyyesuus kiristoos biddeena jireenyaatii
Ortodoksi tawaadiyoon jetteetu amantii
Dhiiga isaa isa qulqulluu nuuf jecha lolaasee
Ofii dhukkubsatee jireenya nuuf laatee
Nuto dhugaa baanaa waa’ee gooftaa keenyaa
Uumaa samiif lafaa jenneetoo amannaa
Qaanii tokko hin qabnu waa’ee isaa faarfachuu
Yesuus gooftaadha jennee kan lallabnuu
Haallee haalle luuyyaa jenneetu sagannaa
Uuma keenya yesuus si galateeffannaa
Amantaan tawaayidoo kan hin moofofnee
Garaa kee kutadhuu yaa diinaa ammallee
Nu barbsiisuudhaaf harka ishee bal’istee
Har’as nu waammattii yaa ijoollee koo jettee
44.SIIF HAA TA’UNAGAANII!
Siif haa ta’u nagaanii miidhagaa foolii urgaa
Imaa Misiraachoo gabreelii ergamaa nagaa
Ulfina qabeessaa koottuu nagaadhaan gara koo
Ifa fannoo warqee miidhagaa yaa gugee koo
Diinni qofumma koo naan mormuf si omee
Sagalee qoochoo kee dhagahee ni rom’ee
Samiirraa dhufnaan na jajjabeessitee
Ifa aalbee keetiin morma koo kan hiitee
Magaalaa ergamootaa raamaarra qubattaa
Fuula waaqaa dura galataaf dhaabbattaa
Hamoonni hin baatanii ifa fuula keetii
Lallabaa misiraachoo fi ulfina waaqaatii
Urgaan foolii keetii abdiidhaan na guutaa
Dambalii yaanni koo jannata daawwataa
Mallattoof dhugaadhaa kochoo kerraa qabda
Eegumsaaf kennaa kooulfinni kee adda
Siif niajajamaa abiddi boba’aani
Gabreel dhaameeraa aalbeen kee xuqnaanii
Kanaaf sin waama har’as dafii koottuu
Leeyya’e seexannii abdii haa kutatuu
45.HOREIYYEESUUS !!!
Hora iyyeesuus(X2)him gelila(X3) abe yordanos
Hede Iyyeesus(X2)   “  ke gelila(X3)wede    “
Iyyeesuus lixemaq maxa ke geelila
Yoordaanoosim sheshe yede weda wo’ala
Tafawase(X3)ye Addaam lij ba mela
Ye bayirii amlaak Igziabiher nawu ale
Manfas qidduus ba igna fit tagalxo
Masakkere(X3)ye waldin kibir
Ye ida dabdabe ale yordanoos
Tawaldo tashare taxamqo iyesusi
Tasaraze(X3) ye Addaam lij kiisi
Misxira sillaasee taye ba gahadi
Babahir sixemeq Igziabiher wald
Tayizo’al(X3)ba fiqir gamad
46.  TENAGERA
Tenagera Izara tenagera Dawit zemera
“      Kenetu gar taye    “
“      babaret tawaldo     “
“      Ye ab lij iyesus       “
“      kesemayat wardo     “
“      Ijji mensha yezu       “
“      gibu ke girgimu       “
“      gombos kena balu     “
“      ke deju selamu         “
Izra tenagera Dawit zemera  (X4)
Tena gera ba izra masanqo Dawit zemera
“        ba Dawit begena     “
“        yi kebar getachin     “
“        yi wedesal gena       “
“        Alamin ye adane      “
“        ba bego fikadu        “
“        tsidk ina selamno     “
“        Ye geta mengedu      “
Izra tenagera Dawit zemera(x4)
Eeliyas ba seragila seware demana
Demana demana ba seragila
Ye Eeliyas amlak beseragila
Ye israael tebaki    “
Libbee ikulaliten    “
Mistiru awaki        “
Kibir yigebahal      “
Ye alamu matsnagna
Ke yikirtabgera      “
Matehal wedegna    “
Temelisen meta beseregila
Ba debra tabor        “
Eeliyas matsnagna    “
Indi sil mesekera      “
Dagim timatale        “
Israeel ba iyesus       “
Amno indi dinu        “
47.INDA IGZIABIHER YALE !!!
Inda Igziabiher yale manim yelemina
Ilil belu komu le misgana(X2)
Bahir tekefele iski tayi maretu
Dakamoch tsento terememedu
Hayilagnochu iyew teweredu
Ye yaiqob kitir ye mayideferi
Ihewu fererese ye sew lij seyineka
Hayilagnochu biberatetun
Intsenalen bersu degegifen
Yetewerawerawu ye telatechin tor
Meda layi wadko geshs hono Egziabiher
Lesilase yidres misganachin
Teshefe adanyi xillatachin
Bayhir lay si ramad mogas alew isu
Be girmawu sinesa tset yilel nifesu
Ye dingil lij igna mina melkaw
Seali naw yelem yemisenaw
48.KIBRA KIDUSAN !!!
Kibra kidusan yihit kibra kidusani
Mudaye mena gerum(X3)
Ye kidusanu kibir neshina
Insetishalen kine misgana
Ye weledshilign ye hiwot mena
Zinab yalebish tanash demean
Tihtina libsish fikir wubetish
Tsins ye zelilal selamta dimtsish
Isatun waldesh isat akifeshal
Sanzemirilish mache yimeshal
Ye tsehay mawuca misrak honesh
Talakun birhan ayenibish
Ati celimi hiwotachini
Lijish iska ale tsehayachini
Sealilana selamileki
Tamayi tsane be kidaniki
Neyirigbiye misla waldiki
Semayi we midir yeawedisush

49.BA MIDRAWI HIWOT !!!
Ba midrawi hiwot(X2) ba fetena bota(X2)
Mariam titebiken ijochoan zergita
Dingil titebiken ijochoan zergita
Jireenyaa lafarra(2) bakkee qormaatatii
Maariyam nu ha eegdu harka ishee baldhifte

50.MAYIDERA MELEKOT !!!
Mayidera melekot(X2)
Mariami ima bizuani(X2)
51.SI GALATEEFFANNA!!!
Si galateeffanna durboo maariyamii(X2)
Abdii wan nuuf taatef akka kufne hin hafnee(4)
Eeyyee
Osoo sanyii si hambisuu baate(X2)
Abidda akka sadoomif gamoora dhala namaa nyaatee(X4)Eeyyee
52.JAALALAN HUNDA GOOTE !!!
Jaalalan hunda goote nama fayyisuuf fanno irra oolte(2)
Baay’ateera baay’ate jaalalli kee(2)
53.JAJJABAADHAA !!!
Jajjabaadhaa(X2) amanti keessanittis jabaadha(X2)
Sobaan dhugaa bahuun hin danda’amu(4) eyyee
Ni amanna ni abdanna ergamoota waaqattis himanna(X2)
Yeroo rakkinaa fi yeroo gidiraa yeroo dhiphinafis abdii nuuf ta’u(X2) eeyyee
Yaa maariyamii yaa haadha koo dhabbadhu mirga koo(X2)
Ilma kee naaf kadhu waa’ee cubbuu koo X(4) Eeyyee
54.IYYEERUSAALEM GALUUF !!!
Jaalalli waaqayyoo guyyaa jimata fannoo irratti mul’atera
Iyyeerusaalem nu galchuudhaf biyya haaraa(X4)
Iyyeerusaalem galuuf jajjaabadha yeroo hunda ya namoota
Dhiyaateraa dhufaatin gooftaadha (X4)
Enyuu kan qopha’ee iyyeerusaalem ishee haara galuudhaf
Qulqullota wajjiin mirga isaa dhabbachuufi(X2)
55.GALATA WAAQAYYOO !!!
Galata waaqayyoo yeroo hundumaat(X2)
Akka Daawwit anoo garbicha isaati(X4)Eeyyee
Gooftaan koo Amanuu’el baay’ee najaalate(X2)
Seexana harka dhiiga isaan na bitate(X4)Eeyyee
Seexanni haaleyyatu mormituun dinnikooX(2)
Humna gooftaan mo’achuun yoomis kankoo(X4)Eeyye
56.YEROOISINDHUFTAN !!
Yeroo isiin dhuftani(X2)dhuftanii mana waaqa keenya(X2)
Gammada namoota isin simatti maariyaam ati keenya(4)e.
Ega yaa namoota lubbuu keessan(2)waaqayyoof kennaa(X2)
Maariyam haati keenya nu gorsiti kaane dhaggeffanna(X4)e
Hammeenya dhiisaati koottamee(X2)yaa namaa(X2)
Waaqayyoon haa kadhannugalgalas(X2)ganama(X4)eyyee
57.WAA’EE KEEN HIMA !!!
Waa’ee keen hima (X2)Jaalala keen hima
Yaa iyyeesuus isa jaalatamaa(X2)Eeyyee
58. YAA WAAQAYYOO GOOFTAA !!!
Yaa waaqayyoo gooftaa(X2)si galateeffanna
Suma malee kan biraa maal qabnaa(X2)
Yaa maariyaam giiftii(X2)nutoo sii jaalanna
Waan nuuf desseef qoricha fayyinaa(X2)
59.SIDHA MIKAA’EEL !!!
Sidha mikaa’eel israa’eelif(X2)
Mannaa samii buustee(X5)mikaa’eli
Tulluu siina irratti Eeyyee
60. DUBARA KEESSAA FILATAMTEE !!!
Dubara keessa filatamtee kenna waaqarra kan argatte
Gammadi yeroo hunduma(X2)Yaa maariyami abdiin keenya suma(X2)
61.MUCAA KEE BAATTADHUU !!!
Mucaa kee battadhuuti yaa haadha gooftaa koottu maariyami(X2)
Kottu(X2)kottuu maariyaami Eeyyee(X2)
62.YOHANISIN !!!
Yohanisin ye atemeke(X4)
Bahinone(X4)ba mayidoti yordanosi
Iyu tithtinawun ………..yahatemeke
Tsidkun temelketu…….     >>
Ba Bariya iji hono…….     >>
Ye geta timkatu…….   >>
Ante menagn sawu….     >>
Kidus bayitawi….           >>
Ba iju tetemko   ….         >>
Iyesus nazrawi…….           >>
Tasawiro sele……… yah atemeke
Ka alem talayito…..      >>
Awajun simu ale….       >>
Bagon asayito……          >>
Nisiha iye gebu……..   yah atemeke
Iye tenezezu……        >>
Ba yohanis sibkat…   >>
La Igziabiher tegez>>
Ye semayu geta……..     yah atemeke
Midrawi siye temki….   >>
Mistir tegelete…………     >>
Alam hulu awaje……      >>
63.  ILIIL ILIIL !!!
Iliil(2) desi yibeleni
Ajiben metan tabota higuni ilil bilachew       tekebeluni(X2)
Ye kal kidan tabot   ilil  desi yibeleni(X2)
Ye kibru zufani        >>>>
Ke manbaru wardo  >>>>
Iye bereken              >>>>
Kidusu metsehaf       >>>>
Inda negareni           >>>>
Wetan ke sefaru        >>>>
Iye teketelni             >>>>
Ye semayu mekdas   >>>>
Ke lay si kefat         >>>>
Tagalto ayen           >>>>
Ye kibru tabot         >>>>
Ililta zimzre            >>>>
Ina kirb misgana      >>>>
Tabotu lijochun       >>>>
Libarik nawn          >>>>
Ba wust ina ba wuci   >>>>
Baw ark telebso         >>>>
YE Igziabiher cherinat >>>>
Ba irsu lay tegelto      >>>>
Israel be miret           >>>>
Tabot tekelele           >>>>
Tabotu sinaka           >>>>
Bahir takafele           >>>>
Ba Igziabiher tatoch  >>>>
Takarso tizazu         >>>>
Kahinatu yizo          >>>>
Ba sirat sigoazu        >>>>
Wadken insegdalen    >>>>
La kidus tabot       >>>>
Ye Igziabiher sim    >>>>
Ye tetsefebat          >>>>

64. BU’UURA YEEDALOO !!!
Bu’uura yeedaloo eegale (X2)Yaareed lubicha(X2)
Yaareed(X3)Yaareed lubicha(X2)
Qooqni isaa bareedaa(X2) Eeyyee

65.BA FIKIR TASIBO !!!
Ba fir tasibo warede la igna sil
Ye fikiru fitsame ye taye ba meskel
La igna yelerege kato min alena
Afechin zim ayibel ine kirib misgana
Desi yibelen semsyatin kedo
  >>         teteku abetachin
  >>         Ye zemenat nigus
  >>         Iyesus getachin
 >>          Ye ifrata hitsan
 >>          Ye Dawit ketema
 >>          Tawaldo adanen
 >>          Misrach tesema
Ba atiat wust aregagn
Sinor tegosakolegn
Amlakinan geta
Ke mot wust atsinan
Zenawun awuru
La ayizab hulu
Inda Igziabiher yale
Manim yelem belu
Desi yibelen werede ba midi
>>         Selamu liseten
>>        Selam le inante yihun
>>         Bilo le sebekelign
>>         Ba maskel tesekilo
>>         Igna yetagase
>>         Ka siol awetan
>>         Ba fikru yetatamni
Aleluya misgana basemsy
>>>>       ba midir
>>>>       hulum kelay hone
>>>>       la cheru Igziabiher
>>>>       aleluya
>>>>       Ye nafsachin deta
>>>>        misgana inakirb
>>>>       Howtir toat meta

66.TSINU SEMAY !!!
Tsinu semay ye imnat arbegna
Arsema ney(X2) wede igna
Ney ney   phetiros Atinatiwos
    >>        Balalit ye akegnush
     >>       Bilun ke adis
     >>       Tankikesh ye temarsh
     >>       Ba fitsum tihtina
     >>       Ba tsalot ye tagsh
>>            Arsema liyu nesh
>>            Amlak ye meratesh
Ney ney        Wubatim wushat naw
     >>            Dam kibatim kentu
     >>            abti tidar hulu
>>   Alaf wuitu
>>   Nigist mebelun
>>   Satisha
>>   Alamin ba menak
>>  wede gesha
Ney(X2)  Areya
>>        biyesekeyushim
>>        Iwote kiristos
>>        naw bilesh sebaksh
>>       Angatishin basef
>>       Aselifesh setash
>>       Kibirish tegelto
>>       La alem abera
Ney(2)Ariya litihogn
>>    La igna la hulachin
>>    Fatsimesh aseyesh
>>    Talak tagilosh
>>    Alemin dil mensat
>>    Awutonalina
>>    Arsema ati leyin
>>    Ba imnat indintsana
Net(X2)Semayat litogn
>>     La dababay ley
>>     Angatoa feleke
>>     Watat mar dam
>>     Inda kidus phetiros
>>     Tagaloshin fetsemsh
>>     Semayewi kibir
>>     Akilil tekenajitesh
Ney(X2)Hayimanotin ka migibar
>>     Izen indin tsana
>>     Ba dabilos watmad
>>     Tayizenal ina
>>     Watmadun sebabro
>>     yi feta titirachin
>>      Arsema atileyin
>>      Kidist inatachin

67.QAANAA ZAGALILA!!!
Qana zagalila(X2)
Baza basergbet Tagagnteshal dingi ke lijish gera
Geta tagagntehal Ka inatih gera
Idimtagnoch molto tegebazut
Sibalu si tetu wayinu alkobat
Dingil inatachin bezawit alem
Anchi dereshilet honshiw amalaj
Ante iye alehis mefer yelebachewum
Hulum yichelihal wayinun mulalachew
Madigawu bado naw bilesh yetenegersh
Getan ye asesabshiw imabetachin nesh
Ye getan amlakinat yetagalatsebat
Minagna tedele ye dokimas bet
Zare ihew bazi ba sergagnoch bet
Barakat fasasa ba amlak cherinat
Wuha telewito ye wayin tej sihon
Ba qana galila hulachin ayen
Igziabiher ka nore ba makakalachew
Hulle yisetanal yihen mesil wayi

68.YALANTE LANE !!!
Yalante lane man lihonagn
Geta hoyi fikirh liben nekagn
High nebar ye afeen mafcha
Ye mati keyer ante bicha
Astemeribet be markabe
Kalihin bicha ye admit libe
Kenu bi kefa wode meta
Asewutezizh lante geta
Wide libelih shilimate
Betem yante naw sewunete
Daladalkilign yanin gara
Indal mot argegn indalfera
Tsatsatagn zare ya gnan weret
Anten selawuki yenorkubat
Fikir nah lake mar welala
Min hiwot ale kante lela
Qasafachinin qasfehewal
Yanin cinkun ken alfenawal
Nagem ante nw adisu ken
Inzemiralen sit nefiken
69. YE FIKIR INAT !!!
Ye fikir inat ye salam(X2)
Yinafikanal simshin sen tyera sin ker mariam
Ba hiwote wust ba nuroye
Kidamign ka fit ke hoalaye
Tadaladala libe
Anchi alesh ina ka atagebe
Mignote yismer dibik hilme
Lilaf wajabun takakume
Ye geta inat nash
Hayilin ye adergal tsalotish
Tilantim zarem amesgegn nagn
Yelem la nage yemisferagn
Meda yihonal tarara
Lijish silalagn ke igna ge
Indet qeralew kemengedee
Haderaa inate asibenyi
Yemasi ceneqenyi xalati
Ye madedeyi atisxinyi
70.SEALILANA !!!
Sealilana(X3)ihi
Mariami ima bizuani(X2)ihi
Lamignilign(X3)mariami ye hulu inat
Ijigu kebdobign ye nuro kebetu
Aligefa bilo kenina lelitu
Angetetku wede anchi neger indi kena
Ke hulu la geta kirb anchi neshina
Mabakenu yibka liwuta ke tikaze
Ba miljash yi wagad ye yazegn awaze
Alew bayignina libel kena kena
Salsesit la kibrish lisewa misgana
Fitsamewu rake mebkawu ye sedate
Imbayen abish inate imabete
Yi weged ke fite yescenakegn hulu
Benee yi
Simish ba tiwulidu ke mar belay taftoal
Tinishum tilikum mariam(X2) yilal
Inem ba taraye ijochen ansiche
Ihewu zemerkulish kedejish matiche
71.MARIAM BIYE !!!
Mariam biye izamiralew
Inda abatoche iteratalew
Ba yared zema ba adisu kine
Lizemrilet ba idme zemene
Mariam biye besat matateka tatkoal balakine
     >>    Mnfase marikual mahilet tegenbo
     >>    Ba warku tsina lay arigoal tsalote
     >>    Ba amanuel inat banchiw ba imabete
Mariam biye ba kibir demean tamltoal makdasu
       >>  Dingil  ya anchi milja sibonal wedesu
       >>  Honesh tagegnteshal huletagna semay
       >>   Geta kanchi watoal ye tsidkachin tsahay
Mariam biye Altegibim si terash mar nesh lakenfere
           >>    Selilene iyelku norkugn iska zare
           >>    Tsagsh bête molto tekreferefelign
           >>    Hazanina lekso ke woala keralign
Mariam biye yebala geraye mishigu ferese
        >>        Ba maskel sir kibre inbaye tebese
        >>        alferam ke ingidih alechign maketa
        >>        Kuslen yemit fewus isren yemit feta
72.ANTI ZABA AMAN !!!
Anti zeba amane(X2)rekebk tsega kibra dingil
Ab yekebral le meriami
Ye gishen terara      Zeba aman
Dagim takemteshal       >>
Talakun barakat            >>
Ba ijish cebiteshal         >>
Insegdilishalen              >>
Ye tsaga sigdat             >>
Imabete Mariam           >>
Ye geta inat                 >>
Lihid wede anbesa   Zeba aman
Wede gishen amba          >>
Adirgn inda hitsen          >>
Wede betish ligba           >>
Baraf ba meskelu            >>
Ka dejish metiche        >>
Ye alamin cacata          >>
Hulunim resiche           >>
Irk naw mengede        Zeba aman
Birtu naw degetu             >>
NIgeriwu la lijish              >>
Ye irsu nw gulbatu            >>
Sireku inda ababa              >>
Sel meta ba algaye              >>
Hiwoten adera>>

Nafsi ina sigayen                Zeba aman
Ye masaginushal                    >>
Alem zelelam                         >>
Simish yitefital                       >>
Dingil Mariam                        >>
Ba tesetesh tsega                    >>
Banchi amelejinat                   >>
Lalijochish yibza                    >>
Idme ina barakat                    >>
73.NANA WADA IGNA !!!
Nana wada igna madanialem(2)
Ye hiwotachin metemamagna
Nana wada igna medanialem
Ye tilantu sime      wede igna
Ye zarew shakime      >>
Bante tewedede
Kan bare tanade
Ye hiwotachin metememegna nana wede igna medanialem
Ney ney wada igna mariam
Ye Adam tesfa metememegna ney(X2)wede igna mariam
Ye matsanish fire
Takegne kenfere
Nitsuan mushira
Ye igziabiher tarara
Ye Adam tesfa metememegna ney(X2)wede igna mariam
Nana yiluhal(X2)mikael
Inda amlak yale manehyiluhal nana yiluhal mikael
Ye lalit korar              yiluhal
Ye kenun aroro              ››
Bado ba demean            ››
Adereseken sina             ››
Inda amlak yale mano yiluhal nana yiluhal mikael
Nana wedw igna phawulos nana wede igna
Nana wede igna phexiros nana wede igna
Ye igziabiher kel kuslen fawase nana wede igna phawulos
Ye wangle arbagna
Ye imnatakegna
Sile geta
Tasawa ba kibir
Ye igziabiherin kel kuslen fawase nana phawulos
Ye igziabiherinkel kuslen fawase nana phetros
74.ADUU CAALA IFA !!!
Aduu calaa ifaa fuulli isanii Eeyyee
Ngaadhaan galanii biyya isaanii(X2) Eeyyee
Qulqulloonni gooftaa warri amanamani
Dhugaa dubbisaatif kan ofwareeganii
Jiruu biyyaanlafaa hunduma dhiisanii
Addunya hadhoofte wangelaan jiisanii
Fedhii biyya lafa hunduma dhiisanii
Maqaa iyyeesuus addunyaaf labsanii
Abidda boba’u keessa dhabbatani
Maqaa maqaa caau kanaaf argatanii
Dhagaadhan dhahaman dhugaa lallabanii
Manaa hiidha keessatti raajii hojjatanii
Isxifaanoosin faa biyyicha galanii
gonfoo isa ulfina kanaaf argatani
75.  KUNOO BOJI’AMEE !!!
Kunoo booji’ame harka koo olqabee
Wangeela kee dhugaa addunyaaf lallabee
Eenyumma koof xalayaa baadhee
Ennaan deemuu hidhuuf sabakee
Sagalee kee naaf dabarsite
Ija cubbuu eebban jaamsitee
Jaalalli kee aja’ibimumaa
Si jibbanis hin gattu eenyumaa
Meeshaa dinqii jettee filattaa
Cubbuu jibbuun nama jaalatta
Si filadhee sumatu naaf caala
Abbaa nagaa abbaa jaalala
Naaf galeera si bare amma
Hundeen hin jiru martinu suma
Na mudatus qormanni hedduun
Jaalala keen namu nah in mormu
Nan farfaadha maqaa kee qaphee
Haa socho’uu manni adabbii

76.ARAARSUMMAA ISAANII !!!
Araarsuma isaanii nunoo ni amanna
Gabra manfas kidus maqaa isaa ni wamna
Nuuf kadhatu isanii foonii fi lubbuudhani
Barabaraani
Harka isaani irraa ni eegganna
Wwaqayyoo nuuf laata fayyina
Araarsummaa isanitti amanuu
Waaqayyoo gooftaa akka argannu
Waada ni qabda ati gooftaa irraa
Maalaa nuuf kadhu ati araara
Dhufnerra nuti mana keetti
Jilbeffannerra si duratti
Eenyu qaana’ee si kadhatee
Mana keetti dhufee sitti himatee
Hibboon keenya nuuf hikameera
Nagaa dhaaf nutis dhabbanneerra
Kadhannaaisaanitti ni amanna
Qulqulluu abuhee ni wammanna
Nu eebbisi fannoo keetini
Nutis si waamna kadhannaani
77.TSILAT ZE MUSE !!!
Tsilat ze muse itsa phatos ze sina(X2)ihii
Tsina tsili(X4)ze Aron kayini ihii
78.ARJUMMAAN ISAA!!!
Arjummaan isaa nurratti baay’ateera(X2)
Haa galatoomu madani’aleem nu fayyiseera(X2)eyye
Cherinatu ba igna lay sile baza(X2)
Yikber yimesgen madanialem ye alam beza(X2)ihii
79.HAMALMALA WORKI!!!
Hamal mala worki(X3)worki
Libsu ye igna mushira hamalmala worki
Ba babilon midir yealtekeketele nw
Ba beta makdas si labsut ayenaw
La kibir ka layu lay tsegaw tedemiro
Molachew mogesu balayechew adiro
Ye mushiraw teren ma azaw yisibal
Ba kiba ba meron ba ixanu kabroal
Yantsebarikalu inda almaz dingay
Barakatin afesu ba mirat iji lay
Bazi alem inku alkebarim zerfu
Ba tsom ba tsalot nw ya ameru margefu
Ye sew iji ayidelem ye tesebebut
Ke lay ye meta nw idifat yelaleba

80.YIBERRAL BA KINFU !!!
Yiberal ba kinfu miljawu fetan nw
Ye amlak sim alebatsimu mikael nw
Ye asedagagn melak zarem kane gar nw(X2)
Ke fite kedeman demana zergito
Indali danager gudgoadun molto
Zare lalohubat birtugulbat hone
Sewu la mabal bekaw mikael degafagn
Ba inate ikif gebiche ba makdasu
Alew iska zare adiron ba manfasu
Ye hiwotin selfoch alefku kesu gera
Tatsifoal ba libe ye mikael sira
Ba zuraye takilo ye isat misoso
Tsidk iye megabagn asedagegn lijun
Ye amlakun misgana zewotir iyestenagn
Irsu nw mikael ba mazmur ye walagn
Fit lafit takilo ke tenashua mender
Yi semagn nebere kinew si derider
Yi wesdagnal liju ye kesekesgn
Talakun barakatba wuste afesese
Sekemin indalay kenfoch gerdo
Meragn wede hiwot medenen wedede
Ye muabin koanka ka afe lay awutito
Ba tsagaw kel kegnegn babarakat molto

81. TAWEIDENAHO !!!
Tawaldina hoo ihim dindili(2)
Sineger neber banabiyat afi
Ba andu ba igziabiher ba andu ba menfas
Andi ken indi hon tsehay indi weta
Yi nafik nw nigus siga labso meta
Abriham yen ken lamayat nafeke
Dawit ba efrata lidatun aweke
Isayas ke dingil si weled ayena
Tinbit tenegere milikit ayena
Kokob ka yaiqob yi wtal sibeli
Semayi honelat inatudingili
Ba hizbu mekekel hono yemiabera
Ba irsu fererese ye celema sira
Ka iregnoch gera betelihem gibu
Kenegistu gar misgenan akirbu
Insiged letsenu yigabawalinaa
Aleqinat silxan becalqanuwuna

82.WAAN INNI DUBBATE !!!
Waan inni dubbate hunda raawwadha
Abdi jireenyaati isa amanadha
Jettee maariyamii haati waaqayyoo
Amanu’eel ilmishee nu waliin jirahoo
Lubbuun koogoofta ni kabajatti
Waa’ee olmasaa hedduu dubbatti
Gatii guddadhan nu bitateera
Ija koo hin kaasu an fannooisa irraa(X2)
Amana malee tasa hin shakkina
Jireenya hin dhumne isaan arganna
Warri ol ofqaban hedduun kufani
Kan gad of qaban hedduun darbanii(X2)
Addunya kana osoo hin umiini
Maariyaam yaadamte yaadangooftani
Sanyiin qulqulluu nuuf hambiseera
Ilmaan addami du’a oolchera(X2)
Waaqayyo ilman isaa waan jaalatefi
Tokkicha ilmasa gadi ergeefi
Isa sodaadha ittin jiraadha
Sagalee abbaa mooti dhugaadha (X2)

83.  MIIDHAMUU KEENYA CAALA
Miidhamuu keenya caala oolmaan waaqa keenya
Rakkina keenya caala oolmaan gooftaa keenya
Nun dagatu nun irranfatu guddan waaqni keenya
Bara baay’eef ture bo’ichaaf gaddaan
Ilmaan keenya qabnus dhoqqetti dhiitani
Jaalala nuuf qabuuf dafee nuuf birmatte
Galaanicha diima kutee nu ceesise
Loltonni fari’oon nu duuka bu’aanii
Nu’iin balleessuf fardaan nu dursanii
Israa’eelin kan eegu yoomillee hin ciisu
Sabasa ceesisee diina kan kuffisu
Beelofnee lallafnaan manna nuuf latteetta
Dhebonne si waamnan bishaan nu obastetta
Aja’iba hojiinkee guddaa jaalallikee
Lubbuu koo gammadi faarsimee waaqakee
Isa abdannee baana isa waliin galla
Yoordanoos nuhin nyaatu isa waliin buuna
Sagalee dubbate iyyarikoo kuffisa
Dhiphinasaf gadadoo nurraa calasaa

84. GALATAN DHIYESSAA !!!
Galatan dhiyessaa anii waqaa na jalaatef
Yemuun dagatame sana isaa na yadaatee
Motichi misir ajajaa basee
Murtoo isaa du’aa narati labsee
Edaa goftaakoo umtee dagatuu
Uumamaa kessaa umtuu sin gituu
Jiraa ajestee du’aa ni kastaa
Lafaaf samirat enyuutu sin fakkataa(X2)
Gaafa rakkinaa laftii hin bari’uu
Yoo bari’eeyumo ifaa hin qabuu
Dhibeen bayyanani haatuu in dagatuu
Mucaa ishee gateetu of ofolchitii
Si malee goftaa koo garin hin jiruu
Osoo naan nufin kan naa gargaruu(X2)
Dhiraa ajjesaa durbaa dhisaati
Yoo babala’ate nurati kaati
Jechuun dubbatee ol of qabuun
Aangoon kan goftaakoo ta’uu osoo yaadini
Du’aaf nu wamnee jireenyaaf malee
Kan nu guddisee enyuu si malee(X2)

85.JIREENYAA LAFARRA !!!
Jireenyaa lafaara(X2)
Baakkee qormatati
Mariyaam nu ha egduu
Harka ishee baldhistee(X2)

86.ULFINAA WAQAAYYOO !!!
Ulfinaa waqaayyoof harkaakoo ol gessaa
Hardhaa refuun ba’ee dukkanichaa kessaa
Yadnii koo deebi’ee enyuumaa koo baree
Karaa jirenyaa wangeelan diriree
Gamana dhabaadheen biyyaa badii sani
Gamatan ilaalee qariniyoorati
Hoolichaa waqaayyoo isaa tsi’oon guubaa
Abarsii seexanaa kanan naraa darbaa
Ajayibsifadhee seenaa enyuumaakoo
Galaana yordanos biyyii dhalootaakoo
Afuraa qulqulluu jedhamaa lammiin koo
Iyeesuus kirstoos kayyoon jireenyaakoo
Isaa jaldheef mitii isatuu na jalaatee
Jireenyaa isaa hin dhumne jedhee nafilaatee
Jalaala isaa argee qaraniyoo irrattii
Boqonaan argadhee faanoo isaa jeelaatti

87. KALLEESSAA NA CESISTEE !!!
Kallessaa na cessistee hardhas na faana jirtaa
Galmee du’aa kooti galagalchitetaa
Jabaatan maqaakee na kasee goftaakoo
Situu Aanaan hobasee gubaata lapheekoo
Kayyoof sagantaankoo sirraati dirirree
Ati na duraa bunaan si teelaan hiriree
Ergaan sii argadhee ulaagan hin gutee
Guutu na badhastee hundarati mote
Wa’ee maqaakeetif hormaan shiraa hin galuu
Sii ganee jiraadhee goftaa du’aa hin oluu
Sii dhaadanoon koo anaaf situ ifajaa
Yeemun sii gonfadhuu uqubaan sif galchaa
Kaayyoon koo si qofa waadan koo hin haara
Situu na lakkofsisee baroota haraara
Maaqakoon naa beekta bakkaan ani jiruu
Kan sii fanaa deemuu tasumaa hin kasaruu
Maaqakoof joruun koo tasaa olmaa kee hin gituu
Garaankoo si bekkaa kan kee himee hin fixuu
Sitoo na filaatee dandiikoo mijjessee
Anis hin wakannee galataa lolassee

88.JARREEN SUN !!!
Jarreen sun aangoo sanittinX(2)
Nut gaaruu waaqa keenyaanii(X2)
Ni Amananaa(X3) isaa andatamuu waaqayyoon qabna
Jequmsii guddaa waraansis ta’ee
Loltuu ormaatin lafti ukkamamee
Ammenyaa bu’aa godhaatan illee
Amantii keenyaa hin xuquu enyuulee
Du’aa kan kasuu waaqayyoo jiraa
Goftichaa qabnaa abbaa haraara(X2)
Loltuu bayyinaan goliyaad ergee
Gaachanaaf Eebboo irratii ergee
Waaqa keenyaan morkatuu illee
Cirrachaa xiqqoon hiree isaa caabsee
Afaan nu guute galaanni guddaan
Nuutis jabannee waaqayyoo goftaan
Osoo Abdatanii fardeen isaanii
Nu harkaa hin banee qaqabnee irrattii
Yoo dhadatanii of tullummaanii
Ni liqifaman galaanichaani
Wa’ee keenyaalee nuuf dhuumee jennee
Du’aa nu olchaa kan Amananee
Sabaa waaqayyoo enyuulee inni xuquu
Jabinnii angosaa amantii saadhaa
Kadhaana qofaan da’oo ni digaa
Waraana afuraa enyuutu faacisaa
Garaa manatii albee deebbisnee
Mo’ichaa ulfinaa nutis gonfanee

89.MAQAAN KEE AJAYIBAA !!!
Maqaan kee ajayibaa maqaa waqaa qabaa
Ergamaa mika’eel sif galataan qabaa
Na gudistetaa atti hamaa irraa naa egdee
Waraa sin qabneef garaan koo na gadee
Jawwichii hin dandenyee surraa kettuu calee
Darbatamee kufee fulaa kee ilaalee
Kanaafan si wamaa atti mirgaa kootii
Simboos argadheraa atoo gartuu kotii
Gargaraa koodhaa atti akka dani’eel
Qorumsaa kessatti garaakoo ilaalii
Maqaan kee wamamnaan dinni ni rifataa
Anis billisoomee qabaadhee galaata
Libaana mana keen urgaa`ee keessi koo
Harkaa keerrabjiraa kadhaaf galaanni koo
Mirgaa waaqaa jirtaa mirgaaf naa jalattee
Halkaaniif guyyaa kanaaf naa dhabbatte

90.FOOLIIN KEE URGA’AA !!!
Fooliin kee inni urga’aa(X2)
Eyyeen mika’eel foolin kee inni urga’aa(X2)
91.KOOTTUU !!!
Kottuu nagaadhanii mariyamii X(2)
Kotuu (X4)mariyami kootuu nagaadhaani
92.SIF HAA TA’UU NAGAANI !!!
Sif haa ta’uu nagaani midhaga foolii foolii urgaa
Himaa misiraachoo gabri’eel ergamaa nagaa
Ulfina qabeessa koottuu nagaan garakoo
Ifaa fannoo warqee midhaaga yaa gugeekoo
Diinni qofummaakoo na marsuuf si’oomee
Sagalee kochoo kee dhageenyaan ni rom’ee
Samiirra dhufuuni na jajjabeesitee
Ifa albee keetiin morma koo kan hiitee
Magaalaa ergamoota raamarra qubataa
Fuula waaqa dura galataaf dhaabbata
Hamootni hin baatani ifa fuula keeti
Lallabaa misraachoo ulfina waaqaatii
Urgaan foolii keetii abdiidhaan na guutaa
Danbaliin yaaniikoo jennata daawwataa
Mallattoo dhugaadha koocho keerraa qabda
Eegumsaaf kennaa koo ulfinnii kee addaa
Si’iif ajajamaa abiddii boba’aani
Gabri’eel dhaameera albeen kee xuqnaani
Kanaafan si waama har’as dafii koottuu
Leeyya’ee seexanni abdii haa kutatuu

93. HAADHA LUBBUU KEENYA !!!
Qoricha foon keenyaa
Haadha lubbuu keenyaa
Maariyaami(X2)burqituu jireenyaa
 Maariyaami  haadha uumaa keenyaa
Haadhoo ergamoota giiftii qulqulloota
Waa’ee cubbuu keenya nuf kadhadhu goftaa
Nun hin dagatin maariyam nuto siti boonya
Kadhanna keen durbee bakka yaanne geenya
Dubaroota hundaa keessa ati kan eebbifamtee
Gammadii yaa mariyaam kennan kan guutamtee
Uumaa samiif dachee garaa keetti baattee
Fayyinaa namootaaf sababa kan taatee
Ergamoonni samii si galateeffatuu
Qulqulleetti jechuun maqaakee faarfatuu
Nutiis si faarsinaa waadaa fayyinaati
Kennaa fannoo jalaa kan nama hundumaati
Haadha saba hundumaa durbee maariyaamii
Ayyaana qabeetti giifti aariyaamii
Galataa keef kaanee nutoo ni dhaabbannaa
Ati nuuf kadhadhuu mariyaam si waamnaa

94.MAARIYAAMII !!!
Maariyaamii(X3)timkite Ze mednii (X3)maariyaamii
Maariyaam(X2) ye hulachin tesfa(X3)maariyaamii
Maariyaamii(X3)abdii hunda keenyaa X(3)maariyaamii

95.WAA’EE KEEN HIMA!!!
Wa’ee keen hima gocha keen hima gaarumma keen hima
Eeyyeen yaa iyyesuus isa jaallatama Amanu’eel fayyisa ilma namaa
Mi’ansaa hunda caala yoo waaman maqakee
Buddeena jireenyati addaadhaa suurraan kee
Booddee hin deebinuu sitti murtoofneerraa
Seenichaa jirjirtee siin bilisuumneerraaa
Jaalalleen akka kee tasumaayyuu hin jiruu
Tokkichaa hundaaf du’ee barri sin jijjiiruu
Qoratee sin baruu beekaan addunyaarraa
Ogummaan hundumtuu barruu keerra jiraa
Aangoon kee guddadhaa abiddaan golgamee
Ergamoota samiin kan galateefamtee
Tokkichaa ilma abbaa tokkicha maariyaamii
Sirraa dhangala’aa Araarriif dhiifamnii
Si jajjadhee hin qufuu laphee koo mootettaa
Otoo hin dhukaasin ana boojiteettaa
Kanaaf sin faarfadhaa mana kee keessatti
Ati na gargaarii bara koo hundatti

96.DU’AA KEESSAA NUU BASTEE !!!
Du’aa keessaa nu baste jalaala keettiin nu wamtee(X2)
Eyyeen galaannii sif haa ta’uu(X2)yaa waaqayyoo

97. MAAL NAMA GODHE !!!
Maal nama godhe Iyyeesuus(X2)homaayyuu
Dhiigasatiin nu bite malee(X4) homaayyuu
Maal nama gootee maariyaami(X4)>>
Fayyisaa hunda nuuf deesse malee maal namagoote maariyami
Maal nama godhe mikaa’eel(X4)homaayyuu
Seexana harka nu baasee malee maal nama godhee mikaa’el
Maaal nama godhegaabri’eel(X4)homaayyuu
Ibidda keessa nu baase malee maal nama godhe gabri’eeli
Maal nama godhe giyoorgisiini homaayyuu
Afaan jawweeti nu baase malee maal nam godhe giyoorgisini
Maal nama godhe Taklayimanot homaayyuu
Itiyoophiyaa hundaaf kadhate male maal nam godhe taaklayimaanot

98.IYYADEGE !!!
Iyye adega(3)le ageritina Ethiopia
Ayitoatim (3)agerachinin Ethiopia
Hin irraanfatu(X3)biyyatti keenya itiyoophiya
99.KIRISTOS TEWELEDE !!!
Kiristos tewelede isey
Kiristos tetemeke bemay weledin
Degim imay(X2)degim(X2)weledeni degim imay
100.BAIDA YOHANIS!!!
Baida yohanis tetemeke iyesus nazrawi
Semayawi (5) iyesus nazrawi
101.HADIGO TESA !!!
Hadigo teas wetesete negad(2)ihi
Maikele bare(2)kome maikele bareh(2)
102.KINEF RIGBI !!!
Kinef rigb bakiburi zegiburi
Begebaha zehani amelmela work(X2)
Anti misraki weweldik tsehay tsidk
Aman be amani(3)
weweldik Kidenik weledite amlak(2)

1O3. BEMENNU !!!
Bemennu be amsale menu nestameselek
Imabete yegna amelaj azegnitua hoo dingily melita wudase
104. MARIAM !!!
Mariam(3)timkita zemedineh(3)mariam
Mariam(3) ye hulechin tesfa(3) >>
Maariyam(3)abdi hunda Kenya(3) >>
105.AKLILE TSIGE !!!
Aklile tsige mariam
Qetsele mengistu mangistu le giorgisi
Kibebe gera work work akilele tsige
106.MEAZA SENAYE !!!
Meaza senaye senaye ihi
Mikael meaza senaye(2)
107.KEME TIBERIKENE !!!
Keme tiberikene be meskelike ze work
Tewenai be tsedk(4)mikael melmale work
108.YAA WAAQAYYOO !!!
Yaa waaqayyoo siyaa galatu
Yaa waaqayyoo maqaan kee haa ulfaatu
Lafa jalaas taanaan samirra kan balali’u
Yoo barbaanne hin jiru kan amma waaqa keenya gahu inni hunduma irra caala galanni isa haa gahu
109.NU JAJJABEESSI !!!
Akka anaaniyaa akka azaariyaa akka misaa’eli nu jajjabessi(2)
Nu jajjabeessi(2) amanta keenyanis nu jajjabessi
Inda azaria inda anania inda misaeli atsinan ignan atsinan(2)ameldin Gabriel

110,YOO FAYYUU BARBAADDEE!!!
Yoo fayyuu barbaddee barbaadde harka daabiloosi
Iyyafadhu dhaqii laga yoordaanosi(2) si baasa harka dabiloosii
111.DHIISI DHIISI !!!
Dhiisi(2) yaaobboleessa biyyi lafa nama goyyomsa
Babbaredee(2) abidda dhumni isaa
Abidda na buusuf yaada jira seexanni dinni koo
Na eegi ati(2) maaloo yaa waaqayyoo
112.MISLE MIKAEL WA GABRIEL
Misla mikaelin wa gabrieli ney senyitiye mariami(2)
Ney(8)imamlak ney mariam
Mikaa’eli fi gabri’eeli wajjin koottu hhadha waaqa maariyamii
Koottu (8)haadha waaqa durbee maariyaamii

113.INZA TAHAKIFIYO!!!
Inza tahakifiyo le hitseniki ney mariam
Ney(20 mariami(2)
Mucaa kee baattadhuuti yaa haadha goofta koottu maariyami
Koottu (3) maariyaamii(2)
114.YAA WAAQAYYOO !!!
Yaa waaqayyoo ati naaf eebbisi bara jirenya koo(2)
Ati naaf eebbisii(2)bara jireenya koo

115.DU’A KEESSA NU BAASTEE!!!
Du’a keessa nu baste jaalala keetiin nu waamte(2)
Eeyyen galanni siif haata’u(2)yaa waaqayyoo

116. DURAANIS KAN TURTEE!!!
Duraanis kan turtee amantaan tokkuma Ortodoksidhuma eeyyen ni amanna ni abdannna daandiin isheedhuma

117.  IJOOLLEE SADAN!!!
Ijoollee sadani abiddaa kan baastee(2)
Labooba bal’isee(2)gabri’eel abidda nu baase
Selastu dekik ye aweta ke isati
Ignanim adinan(2)like melaikt
Ignanim adinan(2) gabrieli like melaikt

118.AKKA IYYOOB!!!
Akka iyyoob  obsa kee naaf kenni}
Na qoraa jira diinni koo seexanni}(2)eeyyen
Akka karaa irran hin banne          }
Akkan si dura hin banne harka na qabi}(2)

119.SILLESE WEREDU !!!
Silese weredu wede abriham bet hono ba andinat(2)
Weredu wede abriham bet(4)
Sillaaseen bu’anii man Abrihaamitti tokkummaan ta’anii(2)bu’anii man Abrihamitti(4)

120.SERAWIT !!!
Serawita melaiktihu le madanialem yikewimu(2)
Ye madanialem agelgaochu yikomalu ke fitu(2)agelgaochu

121.BA QANA!!!
Be qana zegilila(2) ze gelila
Kibkeba kona(2)
Qaanaatti eeyyee(2) gaalilaatti(2)
Ciidha ta’ee eeyyee(2)


122.KIRKOS IYELUTA!!!
Kirkos iyeluta ye awta ke isat(2)
Ignanim adinan(2)likemelaikt
Ignanim adinan gabrieli like melaikt

123.ANDEBETEMYEWUTA !!!
Andabatem yawuta yemisgana kine
Ye amlakin medan ayichealew ba ayine
Ba ayine bagabani semayi tsehayin ye akome
Zarem gobgnitognal iyedegegeme
Watmad tesebere inem amelatkugn
Ka atiyat filatsa ka mot aterefegn
Ye anabistun af ba hailu ye zega
Ye Daniel amlak yinoral kane gar
Ba dawit misgene ba yared zimare
Ka kidusan gera lizemir abire
Irsun semasegin milkol bitsekibign
La getaye kibir izamiralewgn
Asferiw nebalbal isatu binedim
La taot ansegdim nagestet biawijum
Hulu bitewugnim bitelegnim alem
Tsinat yihonagnal geta madanialem

124.   BAKARANIO !!!
Bakaranio ye motewu bezachin nw(4)
Ye motew(2) bezachin nw(2_)
Adisun biftet tsehadw iyesus nw(4)
tsehadaw(2) iyesus nw(2)
Antsegn yitebegn ke atiate cher mehadanite(4)
Ke hatiate (2)  cher medanite(2)
Ye siga tilin ye aferese geta negese(4)
Ye aferese (2)  geta negese(2)
Ye hiwot iras gulilat ye mirat beti(4)
Gulilat (2)ye miret beti(2)
Ye mot abegas teshenefe kestu tetefe (4)
Teshenefe (2) kestu tetefe(2)
Liyu sitota liyu tsega ye dingil lij ga(4)
Liyu tsega(2) ye dingil lij ga(2)
Ba wudi liju sile ayeni atsedekeni(4)
Sile ayeni(2) atsedekeni(2)
Bizu misgana tekegnulet temesgen belu(4)
Tekegnulet(2) temesgen belu(2)
Ba fikir sibo akeberen kef aderegen(4)
Akeberen(2) kef aderegen(2)
Adisun miraf ye kefatew geta moto nw(4)
Ye kefetew(2)geta mote new(2)
Ye mot medanit selamawi degu semrawi(4)
Selamawi(2) degu semrawi(2)

125.ELSHADAYI MAQAAN KEE!!!
Elshaday maqaan kee ni dandeessa
Dirreetti nu baste golga keessa
Ba’aa koo batteetta dadhabbi koo
Kan akkakee hinjiru yaa goofta koo
Lafaa onaa keessa yoo na waamtu
Huccu koo bututee kan jijjiirtuu
Haraabefta fuudhee uffadheera
Jaalala abbummaa kees hubadheera
Gaalila irra mitii jireenyi koo
Hojii guddaan qaba yaa gooftaa koo
Hoolota waqayyoo eeguu kootii
An bara koo hunda kan gooftaati
Waanta ani hin beekne naa gooteetta
Daandii qulqullotaa na dhaabdeetta
Kan akka kee arjaan hin argamu
Gara fayyina irratti kan na waamu
Karaa deemasiqoo otoon deemu
Sagaaleen dhagayee kan na waamu
Saa’ol jechuun hafee phaawuloosii
Na booji’eerahoo kiristoosii

126. YE KIDAN TSILAT!!!
Ye kidan tsilat yetesewera mena yalebish
Dabtara dinkuan anchiw nesh
Iyewum mena yetebelew(2)
Ba dingil mariam ye aderew
Ye igziabiher Ab lij nw

127.ISEY SILETE SEMERE!!!
Isey silete semere(4)
La madanialem negirew nebere  isey silete semere(2)
Barihin si ankoakoa towat ina meta
Tsimen shirehilign molahign irketa
Ba godele bakul ante komehilign
Kifu zemen alfo zaren aseyehign
La tsedkane mariam negiret nebere isy silete semere
Idajua ley kome negiret simeles
Tefatsimo agegnew ye libe filagot
Imabete mariam kanes atileyign
Zewotir ayishalew gadayen sit moy
La kokiyilish mariam negiret nebere isy silte seme
Azene balebeh inbayen abese
Ye gobete kenaw kuslem tefewese
Ye kokilish mariam ba imnat ba tsebalsh
Agenite rida sitere simishi
La kidus mikael negirew nebere isey siletesemere(2)
Ye moten dabdabe ba hiwot keyir
Ye anbasochu gudgoad fetineh yederesk
Abate mikael zarem atsinanagn
Mangistun indi wersi miljah yaguzagn
La kulubi Gabriel negirew nebere isey slte semere(2)
Ye kulubi Gabriel honelign gulbat
Ke mengede indelker gotetogn telete
Mebawun tekife ba ililta indi wota
Ba fit kidemina godanayen atsina
La taklaimanot negirew nebere isey silete smere(2)
Asebe molalish shakime kelelegn
Tselot tirufate ka mot seweregn
Ke debra libanos ke dejih si dersi            Tsinu barakat be hiwot yifsesi
La madanialem negirew nebere
La tsedkene mariam negirew neber

128.YAA GARA  LAAFEETTI !!!
Yaa garaa lafeetti kan nama hunda jaalattu(2)
Yeroo hundumaa(3)fakkatti(2)biiftu kan ganamaa(2)
Hoo ririhta hilina afekirota limad(2)
La ilegisimu(4) timesili(3)ingida (2)
129. DU’A FANNOOSATIN AJJESEE 
Du’aa fannoossatiin ajjesee(2)
Fannoo isaa tiin namootaa fayyummaa nuuf hire(4)

130.DHUGUMA DHUGAADHA !!!
Dhugumaa dhugaadha (4)
Ajaa’ibumadha cuuphamuun gooftadhaa(4)
Aman baa man(4)
Mankire sibhata timketu(4)
131.SAMIRRAA NI BU’EE!!!
Samirraa ni bu’ee dhalatee durbee maariyaamirraa(2)
Foon dubroo maariyaamii(2)uffatee addunyaa fayyisuuf(2)eeyyee(3)
Imsemayat werede wa imariam tewelde(2)
Kama yikun beza (2)wakulu alemi walabsa siga mariami(2)ihii(3)
132.URJII DHAM DHUFANII!!!
Warri hayyoota dhufani(2)urjii hordofani(2)
Amanu’eeli fi(4)sagaduu fi amanu’eelifi(2)eeyyee(3)
Ba kokob matsihu(2)seba segel(2)
La amanueli(4)yisgedu la amanueli(2)ihii(3)
133. QALBII HAA JIJJIIRRANNU!!!
Qalbii haa jijjiirrannu cubbuu irraa haa faagannuu(2)
Namoota waaqayyoo hojii dhaan haa taanu(2)
134.   JECHA KEE DHAGAHUUF !!!
Jecha dhagahuuf goofta laphee koo naaf bani(2)
Laphee lidiyaa(3)akkuma banteefi(2)
135. SEENAA KOO HAARESSII!!!
Seenaa koo haaressii gooftaa naaf geeddarii
Akkan siif hojjadhuuf ati na gargaari
Nagaan baheen gala ergan si waammadhee
Maaltu nan mormaree anoo sin filadhe(2)
Gargaarsaaf human koo naaf ta’I jabina koo
Kan natti hir’atee naaf guuti hir’uu koo
Cubbamadhan turee hunda dadhabsiisee
Gooftaa tu na waame fayyina naaf labsee(2)
Dani’eel gargaartee baafte afaan leencaati
Naanis  na baafadhu du’a badiisaati
Cubbaama qulleessuun siif amala keeti
Nan dhabsiisin maaloo eebba man keeti(2)
Israa’eel gargaartee kan baafte gibtsiiti
Hunduma kan gootu dhuguma waqa ati
Gochakee yommun yaadu guddan rajeffadha
Maqaan kee haa ulfaatu ati waaqa ulfatadha
Inni kana godhe har’as jira gooftaan
Na gargaara yoomuu ani isa waammannaan
Yoomaan himee fixa gochaa inni naaf godhe
Galatan galchaafi maqaa isaa waammadhee
136.HIN CALLISINAA!!!
Hin callisinaa waaqayyoon galateeffadha(2)
Qulqulluu (3)dha jedhaa
Ergamoonni hundi galata jalqabaa
Qulqulluudha jedhaa
Maariyaam haadha musee kabaroo qabadhu
Aarsaa galataatin israa’eel waammadhuu
Gooftaa haa kabajnuu ililleef gammachuun
Nu wajjinin ta’a mootichi mootota gooftichigooftota
Umaamni sagaleen samiin farfaannaan Qulqullummaa isatin hundinu farsani
Yaa daawwit olka’I tsiyoonin farfaadhu
kabaroo rukuti bagana qabadhu
Lammii koo haa farfannu ulfina waaqayyoof
Olmaansaa baay’eedha jaalalli nuuf qabu
kan fayyina argattan ililleen farfaadhaa
Gooftaa goftootaf mootii mootii moototaf
137.  ZEWEYINEH !!!
Zeweyineh(x2)ebête kena zeweyineh(X2)
Ebete kena(X2)           zeweyineh(X2)
Ba kenawa mender             >>
Sergeetedegiso                    >>
Wayinu tesenadto               >>
Irasu tekediso                      >>
Dokimasim tera                   >>
Deka mezamurtu                 >>
Iyesusin ina                         >>
Mariam inatu                      >>
Si belu sitetu             zeweyineh
Ijig des alechew                >>
Ya amangna wayin           >>
Iye tefetachew                  >>
Ililtawum damkoal            >>
Mushirawum kortoal         >>
Sergu la ingidochu            >>
Ye beka meslotal              >>
Wainu bamakekel                      zeweyineh
Aleke ke genu                                >>
Afro tedebeku                                >>
Aselefi hullu                                   >>
Manim sew seyinegrat                    >>
Ihenin teredta                                 >>
Dingil litemalid                              >>
Hedech weda geta                         >>
Genochun mulu alewachew   
Wuhawun kedtachew            >>
yilachual lije                          >>
tazazut amnachew                 >>
bila sitineger                          >>
aselefihochu                           >>
amno guada gebu
tamolu ganochu                    >>
madigaw sikefat                    zeweyineh
melkam wayin hone                   >>
yekiristos kibir                           >>
bebetu gennene                          >>
yeimamlak tselot                       >>
tarukun keyere                           >>
menagnaw behaddis                  >>
yehew teqeyere                          >>
zarem ledekemu             zeweyineh
alecha lehonu                        >>
lenefsachew tafac                 >>
alqobachew wayinu              >>
dingil tiqomalech                  >>
sila innasu tegta                    >>
inditafitunna                         >>
lemmina ka geeta                  >>
lijiwam dinq adrag new          zeweyineh
ullum addis arguwal                      >>
celleman geltuwal                         >>
errarun ataftuwal                          >>
ullem diq adragi                           >>
zarem tamiregna                           >>
ganuchun inniteb                          >>
innimeles ingnam                         >>

138. ARAARSITUU MAARIYAAMII!!!
Araarsituu maariyaam araarsituu (x4)
Araarsituu   yaa haadhaa garraamii
“                  Durbee maariyaamii
“                 Yaa gara -laafetii
Araarsituu maariyaam araarsituu (x2)
Eenyu jedheen waamaa maqaakee
Maariyaam natti ulfaatee gochaankee
Araarsituu  yaa haadha jaalalaa
“                Sumatu naaf caala
“                Yeroon waa hin qabnetti
Araarsituu maariyaam araarsituu (x2)
Eenyu jedheen waamaa maqaankee
Maariyaam natti ulfaatee gochaankee (x2)
Araarsituu   yaa gara-laafetii
“                  Diina nan famatee
Araarsituu maariyaam araarsituu (x2)
Eenyu jedheen waamaa maqaakee
Maariyaam natti ulfaatee gochaankee(x2)
Araarsituu         kootuu mee gara koo
“                        Yaa haadha gooftaa koo
“                        Laali hir’ina koo
“                        Guuti hir’ina koo
Araarsituu maariyaam araarsituu (x2)
Eenyuu jedheen waamaa maqaakee
Maariyaam natti ulfaatee gocgaankee (x2)
Araarsituu         baay’inni yakka kootii
“                        Gooftaattii na hin butuutii
“                        Kadhannaa koo fuutee
“                        Gooftaa gurra buftee

139. DURSII GOOFTAA DURAA KOO !!!
Dursii gooftaa duraa koo
Amanu’eel waqaa kooUmaa koo  umaa koo
!!!eyyeen!!!
Dursii atii duraa koo (x4)
Gooftaa iyyasuus ha qana’uu dinnii koo
!!!eyyeee (x3)!!!
Sootrosaa biqiilaa
Maariyaam giftidhaa (x2)
!!!eyyeee !!!!
Gannatnii cufamnaan sababa hewanin
Kunoo nuuf banamee durboo maariyaamiin
Eyyeenii giftii mariyaamiin
!!! eyyeee (x3)
Nurraa addaa hin bahinii
Egumsaa keetinii keetinii
!!! Eyyee!!!
Mikaa’eel(x2)gargaraa dani’eel(x2)
Eyyeen mo’aataa saaxna’eel
!!! eyyeee (x3)
Arseemaan jabaattee
Mootii dirxaadisin moo’attee moo’attee
!!! eyyee (x3)!!!!!!

140.NAMOOTAA HAA GAMMANNU !!!
Namoota haa gammanuu waaqayyoon kenyaanii
Bittaa cubbuu jalaa isaa nuu baasenii
Ka’aa galatessaa gochaansa baay’eedha
Kan isaaf deebisnuu galataa duwwadha
Kufee kanan ture dhukkubaa cubbuuni
Kufati koo keessaa naa baase gooftani
Wanti ati naaf gote gochaan kee baay’eedha
Kan isaaf deebisnu galataa duwwadha
Akkaa barxemi’oos jaama kanan ture
Har’aa dhiiga gooftaan ifaa argadheera
Seerri kee karaa koof ifaa naaf ta’eera
Kansaa waanan ta’eef nageenya argadheera
Waamichaa keerratti dhugumaa naa waamte
Bittaa seexanarraa bilisaa na baste
Alfaa fi omeegaa baran kan jirattuu
Amaanu’eel gooftaa koo yaa waq si hagalatu
Yakkaa koo karaa koo gooftaan naaf dhiseeraa
Hojii fayyinaa isaa ijii koo argeeraa
Arjummaansa hin dhumuu ulfataa gooftaani
Maqaasa olkasee farfaadha ililleenii

141.HAADHAA WAAQA KAN MADAANALAMII
Haadha waqaa kan madaanalamii koottu maariyaami
(x2)
Kani madaanalamii (x2)    koottuu maariyaami
Maddaa qulqulleetii                    >>>>
Taalilaa hin borofne                   >>>>
Hadhaa gafaa raakkoo                >>>>
Kan hin sisnnofne                       >>>>
Abdii si godhaane koottuu maariyaami
Kan hin dukkaanofnee          >>>>
Maqaa kee waamanne           >>>>
Koyyaa mogaa dhufaane      >>>>
Nuuf kadhaattii durbee qulqulleeti idoo raakkotii(x2)
Dubee qulqulletii idoo raakkootii (x2)
Ilmaa Koo naanii jechaa       idoo raakkootii
Sagaal naa mil’ate                      “”
Garaa lafettii Koo                       “”
Yom naa dagaate                       “”
Garaa ishee deebinaan idoo raakkootii
Rakkoo oddefaachuu           “”
Kan keessaa kof ta’u              “”
Argaadhee gammaachuu        “”
Nuu aararsi yaa wadaa fayyinnaa nuu si farsinaa (x2)
Yaa wadaa fayyinnaa      nuu si farsinaa(x2)
Me mal sodaadhaa              “           “
Abdii gafaa rakkoo              “           “
Siilaa sin abdaadhaa            “            “
Waabii qulqullotaa  nuu si farsinaa
Yaa abdii jireenyaa        “            “
Durbee maariyaam       “             “
Koottuu gara keenyaa   “            “
Nuu arasirsii yaa wadaa faayyinaa nuu si farsinaa

142.  ISHOO GOOFTAAN NUUF DHALATE
Ishoo gooftaan nuuf dhalatee qorichi keenya x2
Ifni addunyaa dhalateera ifni addunyaa hundaa
Raajonni raajanii waa’ee dhaloota isaa
Dinqisifachudhan foon namaa uffachuu isaa
Qulqulloonni gooftaa abdiidhaan jiraatan
Kan addaaiidhaf galee waada yaadachudhaan
Addaamiin deebisuuf gara jireenyaatti
Akka bade hin hafnee biyya lafaa irratti
Aangoo irraa gadi bu’ee jaalalaaf bitamee
Dallaa keessa ciisee huccuudhaan maramee
Yakka keenya ilaalee waaqni nu hin dhiisnee
Tokkicha ilma isaa dabarsee nuuf kennee
Jaalalli isaa guddaan ammana hin jedhamuu
Jecha ilma namaan himamee hin dhumuu	Si jaalanna
Si jaalanna si kabajnaa yaa haadha waaqayyoo
Eeyyen waan nuuf deesseef qoricha yaa hayyoo
Qoricha addunya wan nuuf deesseef waaqayyoo
143. Akka Daawwit 
Akka  daawwit baganaanii
Akka izra masiqoni 
Akka maariyaam kabbaroonnii
Sillaasee faarfannaa baraa baraanii
Suraafel kiruubel Ni jajatuu 
Sodaaf oollannaa fuula isaa dhaabbatuu 
Uumamni hundinuu Ni galateeffannaa
Kan isa fakkaatu eessatti argannaa
Maqaa isaan cuubamneemucummaa argannee 
Dhiiga ilmasaatiin bitamnee isaan fayyinmee 
Sillaasee uumaatti nuti Kan amannuu 
Barumsa ormaatiin nuti hin raafamnuu
Haalleeluuyyaa jennaa sillaaseefii 
nu uumeeraa akka waaqeffannuuf
Meeshaa faaruu keenyaa shaakuraanii 
Yeedaloo ergamootaa Kan yaareediini
Afaan keenyaa ililleen guutamee 
Tasumaa hin yeellofnee isatti amannee 
Yoomiyyuu taanaan isa abdiin keenyaa 
Maqaa isaatiin moonaa diina keenya
144. Gugee Koo 
Gugeekoo garraamiikoo 
Maariyaam ati qabeenya Koo 
Nan furamee ati qoricha keenyaa 
Ulfatoo utaalee nagaa kee dhageenyaan    
Kennaa kennaa caaluu Naaf laatte haadha Koo 
Kanaaf daddabalee si faarsa arrabni Koo 
Gugee Koo siin jechaa garaa kootu hin obsuu 
Jecha Koo kamii Kan garaa si ciibsuu 
Lafee keerraa lafee fudhatee dhiigakee 
Fayyisaa ilmaan namaa baate cinaachi kee  
Golga utubaa abiddlaa museen arge sidhaa 
Abiddi waaqummaa sin gubne dhugaadhaa 
Maxis jennaan gammadde lubbuun Koo 
Biiftuu barii baatuu fakkaatte gugeekoo
Deebi’e hin gahaa maariyaam godaansitee 
Nageenya akka argannuuf nuti ijoolleen kee 
Kan museen dugda isaa argee naasuun kufee 
Simboo kee jaalatee garaa keetti hafee 
Gadi of qabummaan kee ol si kaasisee 
Ulfina hanga hin qabneen mooticha Kan deesse 
145 .ERGAAMOON SAMII
Ergamoonni samii siif safeeffatuu 
Ilmaan addaam martinuu maqaakee safeeffatuu 
Yaa haadha waaqayyoo Haadha hunda keenyaa 
Guyyaa dhumaa Sanaa si wabiin keenya 
Iyyaaqemii fi Hannaarraa wareegaan Kan dhalattee 
Xurii fi badii malee mana amantaatti           guddattee 
Faanu’elii si sooree nyaata samiirraa fidee 
Koochoo walitti; reebee gbri’eel siif gammadee 
Daawwit waa’ee kee raajee qulqullummaa kee himee
Ulfia haadhummaa kee dhalootaaf dhaamee
Maariyaam maariyaam siin jennaa Kan abbootarraa ganamaa fi galgala daballee daddaballee
Bakka yaadannoo keetti dungoo harkatti qabamnee 
Tokkos, lamas, sadiin walitti gurmmofnnee
Yeroo si waamnu koottuu nu eebbisi yaa durbee 
Akka abbaa efireemii
Yaa mootittii ulfinaa dhaabbadhu fuula ilmakee 
Ganamaa fi galgala nu araarsi mucaakee 
Huccuukee warqee sanaan faayamiitii miidhagii 
Keenyas cubbuu fuulasaatti kadhannaa keetiin diigi    
146.  Alfaaf Omeega
Alfaaf omega waqayyoodhaa maqankee
Jalqabaaf dhumaa hin qabuu barii jireenya kee
Motummaa keraa baraan nii jirataa Ni jiraataa 
Sifii lanaa goftaa arsaa galaata
Barrotaa jijiirtaa atti hin jijiiramtu
Angoof human kettiin hundaa Kan rawatuu
Baraan atti yaawaqaa sanumaa 
Dorgomaa hin qabduu goftaa tasuuma 
Kasnee baganaa masinqoo
Qabaneraa tsinatsilif kabaaro
Hunduu silaasedhaaf galataa dhiyeesinaa 
Uumamin martuu issaaf jilbefaana (2) 
Hunduu sif bitaama siyiif abbomama
Ummamni martinuu gudduma kee himma 
Laffiitif samii hojii harkaa ketti
Waqaa waqoota motiidha attii
Waqottaa jedhamun Kan waqeeffaman 
Burkuta`aniru hardhaa iddoo hin jiraan 
Atti garuu baraan nii jirataa 
Sif lanaa goftaa arsaa galataa 
Qulqulluu qulqulluu jedhamuun farfaamte
Galaatan marfamtee Kan waqeeffamtee
Sii qoffaadha hundaa Kan danda`uu
Maqaa ketiif galaan haa ta`uu
147.  DHADANOON KOO SIYII
Dhadanoon Koo siyii yeroo hundaa 
Naaf bafteeta benyaa addaa 
Iyyesus fayiisaa lubbuu Koo
Dhigiin kee baleesee abarsaa Koo 
Motumman samii irraa Kan ittin dhaalamuu 
Boqonaa haraatii Kan ittin cee`amuu
Foniif dhigaa kettuu anaaf gaala ta`ee 
Abarsii dhalootaa issaan qulquula`ee
Affuraa kee jiraa keessaa qamaa kotti
Kanan sin walbaree iyyafaanon mitti
Dha`anan onnee Koo siyyiin to`ataamaa
Wan hundumaa dhisee anii sifaan abbomamaa
Calaqiisaa mussee illaluun hafeera 
Andaqiin dukaana karaa keen haffeera 
Dinii kan facaasee sumii kessaa kotti
Naa fayiistee goftaa olbatee fannooti
Dhigiin abeliidhaa ini dhangaala`ee
Hardhaas nii iyyataa dhiibaan irraa  gahee
Yaa iyyesuus kan kee dhiffama dubbataa
Fayyisaa lubbuu koo hoo fudhuu galataa
 
148.   RAJJII ULIFINII KEE
Rajjii ulfiin kee humnii waqayyoo
Humnii waqayyoo sii golboo 
Dhugaadhaa ergaamonii sittii marisan 
   Yaa midhagduu akka adduu 
   Anoo sin qabaa homaa hin barbaduu 
   Hunduu yeroof qabeenyii aduunya 
   Jaalali kee haa mo`uu mariyaam laphee Kenya
Sinan jedhaa qulquuletii 
Anii jaalalaa ken boji`ameti
Ossoo eggani bayyeen baduu Koo
Naa gorfamteeta naa wamtee hadhaa Koo
Balibalitii ishee cufamtuu
Jedhee dubataa rajjichii isqeeltuu
Waqiini ittiin senee ittin baheraa 
Gonkaa ittii hin senee namnii Kan biraa
yaa fakatuu ulee lemaani
abdii hin qabuu anii sii dhisnaan 
kee ebbaati attii badhaasa addaa 
gonkaa sin dhisuu mariyaam sin jaaladhaa

149.  EGNAA INZEEMIRALEN
Egnaa inzemiraleen telat yicenekal 
Yee destaachewu mincuu kee wedeet nw yilaal
Ye selam mefsesha anchii nesh destachewu
Yee meskel sir sened marayaam inatachiin 
Bee libachiin destaa fitachin yee beraa
Silet senseletuun lijishi sebrolign nw
Mot meshagerachin dilidiy kee mekera
Yee miseaq lij tseayi yegna tinsa`ee nw
Yemedanit mesgeb yee kuslachin tenaa
Ke irstuu indan godiil bee tesfaa indin tsenaa
Lijua desta lem ye destaa minchi hona
Azen besua rikual silee azenuu tasnaa
Yee liqee kayinatuu ye kirstoos inaat 
Irsuu zinab sihon isua demenaa nat 
Sii tebik iregna sii riben beg yalinew
Alfaa inaa omega ye dingiil lign  nw 

150.  NII CUPHAMEE
Nii cuphamee iyyesuusi
Yohanisiin yordanositii
Argaanera bilisuummaa
 Kan nuufi kenee ilmaa waqayyootti
Samii irraa gadii bu`ee    yordanositii
Harkaa yohanisin                 >>>
Yordanos kessaati                >>>
Nii cuphaame goftaan           >>>
Garbichaa sexaana                >>>
Garbitii ta`uun                      >>>
Iyyesus dhaamee                   >>>
Humnaa waqayyoon             >>>
Gamojii irraa dhufee       Yordaanositi
Yohaniis lalabee                   >>>
Qalbii jijiradhaa                   >>>
Afuuraan jiraadhaa              >>>
Karaa Kan sirreessee           >>>
Ilma waaqayyootii               >>>
Inni anarra caalu                  >>>
Sin cuupha afuuraani          >>> 
Lammata dhalannee     Yordanoositi
Bishaanii fi afuuraanii       >>>
Deebinee jiraachuuf          >>>
Laphee amantiidhaan        >>>
Sanyii addaam hunduu     >>>
Bilisummaa qabnaa         >>>
Fayyina argannee           >>>
Addunyaarra lallabna      >>>
Mootummaan waaqayyoo   Yordaanositi 
Nuti dhiyaateeraa                    >>>
Qulqulluu yohaannis               >>>
Jedhee barsiiseeraa                  >>>
Amantiin gooftaanis               >>>
Cuuphaanis tokkumaa           >>>
Isatti jabaadhaa                      >>>
Amantiitti cichaa                 >>>
Ijoolleen waloomaa    Yordaanositi
Takka amanneerraa            >>>
Barumsa keessummaa        >>>
Nuti cigaaneeraa                 >>>
Nuuf galeetu malee             >>>
Jaalalli gooftichaa               >>>
Callisnee hin deemnuu        >>>
Beekneetu barichaa             >>>
Ilma abbaa eebbifamaa Yordaanositii
Dhiifama Kan laatuu           >>>
Akka malka tsaadiq            >>>
Luba Bara baraa                 >>>
Dhiifama nuuf godhii          >>>
Jedhiitii na cuubii                >>>
Gooftaan Ni dubbatee         >>>
Yohaannis chuphatii          >>>
 151 .Dhufeera Mana kee 
Dhufeera mana kee dhaapheera fuula kee
Dhaloota hundumaatiif labsuudhaaf mataa kee 
Yaa haadha waaqayyoo durbee maaramii
Sin galateeffadhaa qooqa Koo giingeenii 
Akka abbaa eefireem fuulakee dhaabatee 
Na eebbisi durbee jedhee si kadhatee 
Sugni ilma kootii sirra haa bulu jettee 
Muldh’ii ispaa hidhatee si galateeffatee 
Ati Kan lalistee akka ulee haaronii 
Kan museen si argee osoo hin gubatiinii 
Manna eeliyaasidhaa ogummaa siloondii
Masinqoo daawwitiin sin faarfadha anii 
      Kennaan Kan guutamtee gammadi harmee Koo 
      Qulqulleettiin jedhaa anis dabaree koo 
     Akka abbaa iriyaaqoos galataan si faarsee 
     Anis sin faarfadhaa giiftii gooftaa deesse    
Hir’uun Koo guutamee maqaa kee waammadhee 
Qaana’ee hin beeku maaram si waammadhee 
Arjummaan waaqayyoo si wajjin jiraa 
Bishaan daadhiittillee jijjiiree argineerra.
       152. Waaqayyo addunyaa daawwate 
Waaqayyo addunyaa daawwatee
Sanyii gaarii si argatee 
Maaryam sin jaaldha itti fufee 
Fayyisaan karaa kee dhufe 
Dubartoota keessaa filamtee 
Uumaa kee garaatti baattee 
Ayyaanaa qabeettii siin jedhaa 
Dhaloota keessaa an tokkodha
Abidda waaqummaa baattee 
Suraafeelitti Kan ulfaatee 
Sirraa Nama ta’e haadha Koo 
Qorichi abdiin lubbuu Koo 
Lapheen isaa waan gaarii baatee 
Abbaan hiriyaa Koos si faarsee 
Haadha gooftaa Koo ta’uu kee 
Kennaa fannoo jalaadha atii 
Haadha akka naaf taatu giifltii 
Ilmi kee siin naaf kenneeraa 
Anisoo harkaa fudheera

Danda’adhaan karaa kee dhufee 
Iyyesuus karaa kee dhufee 
Kiristoos karaa kee dhufee 
Maaryam sin jaaladhaa itti fufee  

153.  Ol Bateeti
Ol bateeti durbee mariyaam (2) 
Kabajamtee ergamootadhan 
      Ol bateeti    Tomaas yemuu argee  
           >>>        Ol samii gubaati
            >>>       Kafanaa ishee fudhaatee 
           >>>        Mallattodhaaf inni 
           >>>        Baartotaaf lalabee 
           >>>        Kaatetii jechuun 
Ol bateeti Bartoon gammaadan 
    >>>       Ol bahuu ishee argaani 
    >>>       Akkumaa tomaas
    >>>       Arguudhaaf hawaan 
    >>>       Kadhanaadhaf laguun
    >>>       Goftaa kadhaataan  
    >>>       Du`aa ka`uu ishee
    >>>       Ijjaatin argaan 
       Ol bateeti Yemuu isheen ol bate
           >>>       Kabajaa guddaan 
           >>>       Ergaamon marsaan 
           >>>        Faruuf ilileen
           >>>        Durbee mariyaamin 
           >>>        Kabajaamtuu isheen 
  
  154. CHERNETU
Chernetuu begnalay silee bezaa
Yikeber yimesgeen medani alame
Yalem bezaa 
Ijigii bizuu bizuu tigstuu
Began tekenawulal miretu
Ametsegna teblen bedelegna
Wegenochu argonal motolinal
Tenegro ayalkim uletaa
 Kafachin ayigolim misgana
Simeshim sinega kibir
Fitu inametalen mesmur
Bemeskel teriko tilen
Selamin setonal fewusin 
Kengid ayinorim dikdiku
Tsilmetun wegagula betsidiku
Meshatu newunaa fikadu
Sewu iske meskel mewudedu
Axifiten bediilen bebizu
Tegawu aqirbonal wede isu
Mihirab indemirik ke misraq
Terariken nebere kanate tsidiq
Kesemayu mesgeb golen
Motachin neber xeften
Irsuu be kirstos awun
Ke amets ke Kunene netsiten 
Barochi mebal kerto 
Xelatoch yeqirboch honenal zemedoch

155. GALATAA KEE 
Galataa kee (2) ya waqayyoo galataake
Yaa waqayyoo (2)         galataa kee
Olmaa kee hunduumaf      >>>
Gochaa kee guduumaaf      >>>
Nagaan nuu olchite             >>> 
Nagan nuu bulchitee          >>>
Nutii homaa hin qabnuu    >>>
Wantaa siif lataamuu          >>>
Illilii jedhaa (2) me waqayyoof illilii jedhaa
Mee waqayyoof (2)        illilii jedha
Waqumaa issatif               >>>
Goftuumaa issatif             >>>
Issaa nuu jaalateef            >>> 
Du`aa nuu olfatee             >>>
Bitaa dinaa jalaa              >>>
Issaa nuu bafatee             >>>
Garaa manaa issaat         >>>
Issaa nuu wamatee          >>>
Nuu Eebbiis (2) yaa waqayyoo nuu eebbiis 
Yaa waqayyoo (2)         nuu Eebbiis
Ijjoolle kee tanee               >>>
Dhufneera garaa kee          >>>
Guyyaa affuurtamaaf         >>>
Guyyaa sadeetaamaatti      >>>
Maqaa keen chupamnee    >>>
Muccuuma argaanee          >>>

Akkam bareedii tewahidoon (2)
Iyyesus                  eyyee      Yemuu lalabduu
Goftuumaa issaf     >>>        Yemuu sagadduu
Hadhaa goftaa        >>>       yemuu kabbajuu
Ergaamotaa            >>>       yemuu abdaatuu
Qulquuloota          >>>        wanaa jaalatuuf

Phaphasotaan         eyyee     wan oganamtuuf
Lubootaa isheen      >>>      yemuu ebbiistu 
Daqonootaan           >>>       Kan tajaajiitu
Ayyanotaa               >>>       yemuu kabaajuu
Farfatootan              >>>        yemuu farfatuu

Ummaataa ishee     Eyyee     yemuu barsiistii
Addii uffattee          >>>        yemuu galatoo
Fanoo hidhatee         >>>      yemuu adeemtuu 
Walommaati             >>>      yemuu amantuu

156.  Haa Galateefanuu
Haa galateefanuu (2) waqaa kenyaa 
Galateefamadhaa Kan galateefamee (2)
Kan hin madaalamnedha bayiin arjuumasa
Nuura bahee hin dhumuu danuudha olmaansa
Dukaana ifaan qodee isaa Kan jijiiruu 
Kan akkaa waqayyoo tasuuma hin jiruu
Wa`ee kenyaaf jedhee iyeesuus dhiphatee
Du`aa kenyaa hanbiisuf jirmaa jidhaa batee
Dhiphinaa issaan hafnee jiratotaa tanee 
Cubbuu adaamin dunee du`aa issaan kanee
Dafqaa du`aa dafqee ossoo kufee ka`uu
Abbaa kadhataafi waraa issaa cepha`uu
Maaf hikaa ittii latuu jechaaf dubii issaa
Innoo dhumaa hin qabuu nagaaf araari issaa
Ottoo aboo qabuu mirgaa abbaa dhisee
Wa`ee kenyaaf jedhee Kan gadii of debisee
Jaalalii waqayyoo hagaanaa hin jedhaamuu
Kanaaf baraa baraan haa galateefamuu 
     157. Jabbaa Mottii Nagenyaa
Badhaasaa biyyaa kenyaa
 Jabbaa mottii nageenyaa
Teklehayimaanottii sii wamneeraa
Nuuf kadhuu waqaa kenyaa
       Har’aas Kan nun amantaa kenyaa mogolee jabaanee
      Dandii attii tolchiitee irraa immaalee Kan nuti asii genyee
      Boriis jabiinaaf kadhana keen nii tarkanfaanaa 
      Situu nuuf jiraa sii qabanee maal soddaana
Siluumaa waqayyoo sii filee ijjoolluumati
Wadaa sif galeeraa goftichii samii gubaatii
Araagalfaataa Kan sii qabuu malee hin bela`uu
Namaa mitii laftii kee tasaa hin bela`uu
       Abbaa jabbaa akkaa kee qabnaa Kan nuu nyaachisuu
        Bubiisee qileensii nuu raasee nu hin sodachiisuu
        Hidhanoo kenyaa jabbefaane sin sii lelisnaa 
       Gootaa kadhaanan nuu ararsuu niyii sin qabnaa
Kalawaa kee Kan dhuffee martiinuu eebbaan gutaama
calaqisaa jiraataa malee hin arguu hamaa 
Kanaafiyuu yeroo hunduuma mana kee demnaa
Andaara lafaati kanaf maqaa kee nut dhugaa bana

    158. Kottaa yaa namotta

Kottaa yaa namootaa ni deebinaa
Biyya lafaa kanaa nituffannaa
Guyyaan dhufa gooftaa nuttii dhiyaateera
Waan raajootan dubbatame hunduu raawwateera
Biyyi lafaa kunii maalii bu'aanisaa
Sobee nu goyyomsaa hundumtisaa
Har'aaf nutti tolee jireenyiisaa
Guyyaa dhufa gooftaa nu salphisaa
Hawwii dhaaf kajeellaan biyya lafaa
Mee hubadhaa ilaalaa innii hafaa
SagaleenWaaqayyoo yeroo hundaa
Bara baraan darbee jiraatadha
Wayyee biyya lafaa walaalchisee
Namoota baay'ees ni raatesse
Fedha foonii duuka maraachisee
Ulfina waaqayyoo walalchisee
Amantoonni hundinuumee hubadhaa
Walfakkeessuu dhiisa amanadhaa
Dammaqaa dhaabbadhaa antaadhaan
Jabbane akkaa galuu biyaa abdiidha
159 Kirstos Iyeesus 
Kirstos Iyeesus carraa kottiim atti
Qabanaa argadheeraa gadisaa kee jalaa
Ergaan sitii amanee nagaan bahee gala
Baaruu keraa nyadhee baaruu keraa dhugee
Anii essaa iyyuu hin demuu goftaa Koo sii dhisee
Qorchaa ta`uu kee amaneeraa ma
Madaa baaruu ketiin madaan Koo fayeeraa
Ossoo dinii ilaaluu harkaa naa kachistee
Jirenyaaf barbadee ofiiti naa wamtee 
Anii wa`ee kee hin dhisuu sin farfadhaa goftaa
Afaan dinaa cuftee afaan koo saqxeeta
Dinii naa kufsuuf gufuu natii guraa
Naan dagatiin goftaa sinaan bahee gala
Naan kufaa jedhee wan tokkoo hin yaada`uu 
Ergaa attii naa bate baruu kee irraa hin bu`uu
Naan dadhabee hin jetuu namaa hundaa bataa 
Kunoo sitii hirkadhee hirkoo naaf tateeta
Kan naa busuu hin jiruu sin borafadheraa
Attii wanaa hin rafneef anii rafeen bulaa 
160.Naa Jabbesera 
Naa jabbeseraa humnii waqaa Koo
Hidhee kaa’ee meeshaa afuraa Koo
Nan sodachisuu lolii dinottaa 
Na mosisserraa waqnii waaqoota
Guddinaa foonif mitti lolli dinottaa kenyaa
Yonnaa qabannef malee gargaarsaa waqaa kenyaa
Waan gochuu qabnuu hundumaa Eeyamaa isaa     gafanee
Ergamoota abbidadhaan giddu isaan dhabanee
Meshaa afurra isaa gutanee fannoo iyyeesusin qabanee
Mikaa’el kunoo duraa kenyaa gabri’el nufta’eraa humnaa kenyaa
Bantiin waaqa banamme samii torbanuu keessa
Yemmu gaddi nuf robbanii loltoon akka dumeesa
Ijoolle waaqaf loluu nijaalattu amantoota
Lolaatti Kan bekkamuu hin jirru akka ergamootta
Tamsa’aan nibaadu mormittuu waaqa kenyaa
Calaqqefi abidda isaan darraa ta’u dinni kenyaa
Hirkoo Kan barabaara iyyeesustuu nuuf ta’e
Hulfinnaa waaqumaa isaaf naan farffadhaa ol ka’ee
Akkamittin dubbadha safuu waaquma satti
hinoo bakakkan lolla kakkaween meshaa satti
Dhekkamisaa sagallee satin addunyaan ni rafamtti 
Afurri garggarii cite lubbuun keessa sookitti
161. Turee fakkatuus
Turee fakkatuus sitti barfattu tasumma 
Waaqayyoo keenyaa amanammadha silumaa
Inni jalqabaa xumuuras
Kan nugaggesuu isumaa har’aas
Senaa baddee isaatuu haressee 
Kan dhiphatte Ni boqochisse 
Sutta jedhuus maltuu issa dursaa 
Waqnii kenyaa hundumaa gaggessa 
Dinni keenyaa kiyyoo dirirrsee 
Nuu qabbuf jedhee yoo qayisse 
Humnii isaa turee hundaa durssa 
Waaqqayyo hin gattu ilman issa 
Alii jiruus yoo nuu yadesse 
Goliyadda baay’ee nuu dhiphisee 
Yeeroo dhumeetii cirachaan 
Adda rukkutee mootidhaan 
Qorreen cuffamus dandiin keenyaa 
Eeduu dhiphaatus lubbun kenyaa 
Fullaa issa enyutuu dhabbataa 
Iyyesuus turuus Ni muldhataa 
162 Attii yaa hadhaa dhugaa
Atti yaa hadhaa dhugaa (2) 
Ayyaanaa argatee ulfiina durbuuma 
Mariyaam sif bu`ee afuur abbaa 
Gaaraa gisheen irraa yaa hadhaa dhugaa
Ulfiinan tesetaa                  >>>
Ebbaa issaa guddaa           >>>
Hakaan qabatetaa              >>>
Si`ii ulfiin aduunyaa          >>>
Kabaaja ulfiina                  >>>
Mariyaam giftii kenyaa    >>>
Hunduu sii jaalanaa          >>>
Cimaadha gaarii issaa    yaa hadhaa dhugaa
Fagoodhaa demsii issaa           >>>
Naaf kadhuu ilmaa kee            >>>
Iyeesus umaa koo                     >>>
Akkaa abbaboo biiraa             >>>
Muldhadhee akkan hin bane   >>>
Cinaa koo dhaabadhuu            >>>
Rafamee akkan kufnee           >>>
Naa egii yaa hadhaa koo yaa hadhaa dhugaa
Naan dhufaa manaa kee        >>> 
Naa simadhuu adaraa            >>>
Harmee Koo mucaa kee        >>>
Yadaanno ilmaa kee             >>>
Qabadhee fanoo issaa          >>>
Hin qana`u anoo                   >>>
Ililicheen farfadhaa              >>>
Yomuu sin dagadhuu yaa hadhaa dhugaa
Galmaa koo galgalaa             >>>
Yadaanoo koo durii              >>>
Dandii koo fayinaa                >>>
Naa kessaa jiraa hoo             >>>
Dhiginii ilmaa kee                 >>>
Kanaaf sii jaalanaa                >>>
Wan tateef hadhaa isaa         >>>
163.Ol naa qabdee
Ol naa qabdee mika’el ol naa qabdee
Anii enyuu waltajirra Kan naadhabdee
Dinnii Kan Koo mufaterra dinni Kan Koo
Natii dhabbanani mikaa’el ati maddii Koo
Hin darbayuu hin senee barii rakinaa sunii
Martinuu darberaa mikaa’el si wajiin
Naa fulduraa batee dandii Koo mijeesuuf
Naa jabesitetaa akkaan hin gufannee
Akkaa har’aa mitii jiruun Koo kallesaa
Rakkatadhaa jechuun martinuu naa dhensaa
Madalaa namattin bakkaa hin qabuun turee
Mikaa’el jechuun har’aa ol jedhee
Garaa hadhaa kottii jalqabdee naa eegdee
Ijoollumaa kootiin ------------- 
Jiruu Koo har’aa ati utubadhaa
Kabajaa Kan kettif ansii na dhabadhaa
Hamii kiyaa kanaa innii baraa baay’ee
Kadhannaa keetin har’aa naïf milka’ee
Jalalaa Kan ketiin hidhamee onne koo
Anii hin dagadhuu mikaa’el hirphaa Koo

164.Tallaq behonewu
Tallaq behonewu imnatish tammen kuny
Kalleshi bet gasgishe maaxxahuny
Innate kibrishin angishee
Sew honkuny inde itsan taddishe
Innate qidist arsema zinnash le alem tesema

Simaxa be alga nebere
Tesfayem yeteseber
Be imnat betsebelish
Sew honyee qomkuny dejish
Linager zinashin lawura
Yideneq ye amlakee siraa
Tegadlosh ye imnatish tsinat
Hononyal ye imnatee mabrat

Demgibat kentuu bileeshi
Ye semay kibrii yetaceesh
Ye inmate aserafinoot
Be miljash alewuu be hiwot
Ye libun lenegereshi
Fexno yidersal miljash
Zenbabash hiwot yizeral
Yexerash man afro yawuqal

Irdatash yedereselet
Yamexal ye libuun silet
Lamenush fawusish qirb new
Banch afro yehede manew
Yelibuun le negereshi
Fexno yidersal melsishii
Zenbabash hiwot yizeral 
Ye xarrash man afro yawuqal
165.Handarii nagaa
Solganumman kee addadhaa
Ayyaanni kee olanaadhaa
Maariyaami hadaarii nagaa
Maariyaam simattuu hagaa
Magaala nazreet gaalilatti
jibrii fi warqee yoo wal simsiistutti
Gabri’eel dhufee hagaa sitti himutti
Ayyaana qabeetti siin jedheera
Suraafel kiruubel caala kabajii kee 
Ilmaa kee duraatti guttuudha sugnii kee
Warqee Ufaatte mirgaa isaa dhabaataa
Uumamaa hundumarra Eenyu sin qixaxxa
Goddoo dokkimaas hir’umaasa ilallitee 
Hanqinnaa isaatif battee kan kadhattee
Anas muccaa kee durbee naa yaadadhuu 
Kadhannaa keettin hir’uun koo akkaa guttuu 
Guggee garammi koo jaalalan naaf koottu
Wa’ee cuubbu kootif ilmaa kee naakadhuu 
Anoo dadhabbaadhaa namuussa koottin
Aniddarii naaga koo du’aaf nalattin
166.  Haberetang fikri
Haberetang  fikri getahe
haberetagn kindi amlake
Be simi dinyalewu be tsega
Be madariyawu honye si xera
Sadomi sita qaxil mergebuha sibeza
Liteweny hayishaw lijuu indewaza
Higuu be masebe amlak ferredelinyi
Gotitoo yemiya wexa mexak sededeliny

 Be genan mederder hayaqomim xaxe
Ye wencife dingahi Antene gulbete
Ye sa’olin kabba awliqe xellikiliny
Ye filisxemun sewu kind sebereliny
Sost gize sikied alawuqihim biye
  Doro sile cowu tizi alkeny getahe
 Wexahuuy be imba ka ayihud isat
 Ke hadi satileny hanorkeny be fiqri
Samrawii nat sattil kibrin ye sexehany
Inda ante kee ayuud fiqrin man hasanye
Misxiren be mulu negerkeny getahe
ye fiqir wuha qeddahu insirahel xiyye

167. Mexichalew
Mexichalew silat Semroliny (2)
Be gishenuha dingil immebete
Yelemenkuhal ullu tesaktoliny}2
Mexichalew              badohen wexiche
    >>>                         be mulat temelesku
    >>                  inat xerichesh
    >>                  hinema mech haferku
     >>                    gemenahen shefony
    >>                     imbahen habashe
    >>                     silete semere
   >>                      kedejish derishe 
Mexichalewu       yemiskin inat nesh
      >>                  libish yemirarra
   >>                    Azenuyitsnannal
     >>                   Simishin yexerra
    >>                   Tamirish yigermal
    >>                   Tsebelish fewashi
    >>                  Manewu yaldanebishi
      >>                   Metto ke betishi
Libbewa be fiqri  siloshal
Hinate hindet yiresashal
Imamlake hindet yiresashal
Ye mesqel sir tirfe hinate yilishal
Liyu sixotash hinate yilishal
Yimesgen getahe             >>

Mariyam(2) silish           hinate yilishi
Azene yixefal                      >>>
Simish haregagtony              >>>
Selam yisefnal                        >>>
  Ke dejish ye derese be desta temelese(2)      Bedesta                      temelese(2)
Hiyale                               >>
Mariyami                         >>
Hagenye                           >>
Salami                              >>
Hinat nesh                       >>
Le ullu                             >>
Imamlak                         >>                 
Lemilu                            >>
Simish      temelese        yexerral
Hayayim          >>          mekera
Memmekiya     >>          hinat nesh
Ayal qim          >>          wudasesh
169.yegna newu
Yenyanewuu washawu himnatu tsebelu
Anafrim timketachinewu meskelu
Yenyanewu yenya        yenyaa
Ye sostishi amet                 >>
Tarik yalati                         >>
Tabote tsiyon                      >>
Yallechii beti
Ye tsalot sifra
Ye kidan ager
Ethopia hinate
Hagere igziabiher
Ke hadit dingahi              yenya
yete weqerewu                   >>
Ye lalibela                          >>           
dinqi siranewu
Xarawu kift hono
zinab y emayigebawu
Abuna aron                   
mininya wub newu
Ethiopia agare                    yenyaa
Lijish bakosi                         >>
Texemkolishal                      >>
Be filiphiyusii                      >>
Ye amlak sewu mehon          >>
Misxirin awuqo                     >>
Be iyasus amnawu                >>
Mexa texewqo                    >>
Timkhiitachin newu                        yenyaa
Ye geta mesker                               >>
Amnen dinenal                                 >>
Be himnet betsebel                           >>
Meleyachin newu                                >>
Haxiwachini                                       >>
Tewahido nat                                   >>
Himnat achini                                  >>          

Tsadqawe hiduu                           yenyaa
Shenkora hidu                               >>
Gishenim wuxu                                >>
Askumwuredu                                  >>
Shebewu tefetto
Iwiru berto
Gobaxawu qento
Denqorewu semto
Fitshum amnenal
Ayinachi ayitewu
Tsenten qomenal
Joro achin semto         
  169.Qulqulluu  mikaa’el
Hangafni ergamootaa albeesaa qabatee
nu gargaruuf dhufe samii ariifatee Qulqulluu qulqulluun mikaa’el nu wajjiniin jira
Saba esraa’eliinis ceesisee galaana eertiraa
Surraansaa addadha qulqulluu raamaati
Kadhaan kan fayyisu afuura hamaarraatii
Kennaansaa ajaa’iba maqaa waaqaa baatee
Dhala namaa hundaaf inni kan dhaabbate
Leenca fira godhe raajii daani’eeliif
Jabina amantii kan late afoomiyaafi
Nuunis nu hin dagatu nu gargaaraa jira
Araraaf nuuf dhaabbate waaqayyoon fuuldura
     Abbaan baahiraanii har’as kan keenyadha
     Dukkana kan mo’e ergamaa ifaadha
     Gidiraa keessatti inni yoom nu dhiise
     Afuura hamaa irratti kunoo nu moosise
Hiriira samiirraa ofii dursaa ta’ee
Waaqayyoon kan labse mo’ichaan kan ba’e
Diinicha kuffisee angoo kan muudame
Hoogannaa ergamootaa mikaa’el nuu falme

     
  170. Ho Amalajituu
Hoo amalajitu yee li’ul zufan inaatu(2)
Bi’itsit yilishalewu isegilishalewu
Bi’itsit ilishalewu inate bee miljash 
Simtu alfewalewu
Anichiin yaskedeme mech yisenakelal
Miljaash yee redaa sew kibirishiin yaweral 
Lenem anchi iko nesh metamamegnaye 
Was tebekaye nesh tila kelelayee
Yee abewu mahilet yee zotir wudasee
Anachin samesegin tarfalech nebse
Atitefam misganash lee zelalem ke afe
Le kibirish tegadilo ke fit teselife
Aliteretirim be amalajinetish 
Ayichalewuna weyinun asmolitesh 
Amalaje anch feraje lijish 
Sintun asmireshal ke fitu komesh      
171.Simesh selam
Simesh selam meleskiliny
Inbaayen kayinee abeskilinyi
Getaa kafii beeli le zalallemi
Abbaa indantee maniim yelam
Meslony nebaree yeresahinyii
Fitihiin kenee yaa zorkibiinyii
Abbaate maxaa wade maata
Salaam sexxehinyi enee getaa
Lakkasi mazanee labeegonewuu
Mehuxat mewurede la marefnewu
Medaanit honkeenyi le himamee
Iyewuu zemer kunyi fitti qomme
Usxee siseberre be hazanee
Ayalfimi biyye yihe qanii
Imbaayen bahafaas kemeqdesuu 
Salaam yimexxal bee nugusuu
Wusxee be fiqrii yanesahani
Belibee zufaan yane kesehali
Yebeet molaat berekeette
Ye qusilee zaayit medaanite
172. Iyyeesuus ati abbaa keenyaa
Iyyeesuus ati abbaa keenyaa
Dhokkataa kataa jireenyaa
Eegumsaa keetin guddaane
Soorata baruuke nyaannee

Amalaa keenyaa daandessee
Jaalalaan situ nuu gaagessee
Siin daabare isaa kaleessaa
Deemsi keenyaa siin bakkiisaa (2)
Darbamuus qabdetuu nu dhaabde 
Yoo kufnees atii ol nu qabdee
Caba keenyaaf waaldhasaa taate
Millii keenyaa si’in dhaabbatte (2)
Obsaa isaa hin jijjiiramnee
Ogummasi sirraa baarannee
Waa’ee kee yoo dhugaa bannuu
Nu Uummu kee tasaa shakkinuun
Akkaa keeti maaltu nuu baate
Olmaan kee nurraa baayatte
Arihayatam nusii nuti jibbamnee
Abbaa akkaa kee tasaa hin arganee(2) 
173.jaalalaan hundaa gootee
Jaalalaa hundaa gootee 
Namaa fayyisuuf fannoorraa holtee
Baay’ateraa x3 jaalalii  kee  x2
Ya waaqi galataa kee
Garummaa kee himnaa yerumaa hundumaa
Waadaa kee kan egduu mootii amanamaa
Waa’ee cuubuu keenyaaf fanoo jidhaa bate
Fayyinaa nuuf tatee dhiigaa kee lolastee
Ni yaadaan har’as olmaa kee isaa guddaa                                                                              Arjumaan kee hin dhummuu jaalalli kee addaa Jireenyaa akkaa arganuuf lubbuu kee nuf latee
Giddiraa keenyaa hundumaa ofi keef godhatee
Jaalalaa ilmaan namaf fannoorraa oltee
Sanyii Addam hundaa bilisaa kan baste
Gochaa kee ibsuudhaf jechat nuu hanqataa
Ammaa bara baratti ulfadhuu ya gooftaa
Yeruuma hundumaa galataa sif qabnaa
Kanumaa kan qabnuus  kan sif ta’u kennaa
Manaa kee qulqulluttii eebbaaf kan nu wamtee
Kennaa kee hin dhummnee galataan nu guutee
Dhiigaa keetuu gooftaa cuubuuraa nuu dhiiqee
Iddaa du’aa kuutee gatiin nurraa haqee
Kanaaf sif hiriree sif addaa bannerraa
Jaalalaan nuu binaan galataaf kanerraa
174.Sittaan dhisee 
Sittaan dhisee gooftaa homtuu nan yaadesuu
Abdii kootuu si naafoo hunda kan dandessuu
Yoo qorumasaaf saxilamnuu 
Bakkaa dhabnee yoo jibamnuus
Ogdii keeraa hin goddanuu
Siyyin qabnaa hin sodanuu
Enyuut dhabee si abdatee
Baruu kee irrattii of gatee
Kanafanoo si wamadhee
Hinqana’uu si qabadhee
Yoo tureeyu dursaan hin qabu
Kan isaa wamee falaa hin dhabuu
Akkaa iyyoob obseen egaa
Furmataa kos naf ni bekaa
Mijesitetaa duraa koo 
Naf hubateem rakkinaa koo
Siyyi gooftaa gachanii koo 
Sittaan dhisee an waa’ee koo
"""

amharic_words = ['tenagera', 'izara', 'egziabiher', 'igziabiher', 'geta', 'amlak', 'mariam', 'dingil', 'kibra', 'kidusan', 'selam', 'yimesgen', 'amlak', 'medanialem', 'hawwii', 'sillaasee', 'mikael', 'gabriel', 'aleluya', 'hiwot', 'tesfa']

def guess_language(text):
    text_lower = text.lower()
    
    # Simple heuristic
    amharic_score = 0
    for word in amharic_words:
        if word in text_lower:
            amharic_score += 1
            
    # Some specific words are Amharic transliteration
    amharic_indicators = [' yale ', ' yes ', ' nw ', ' liyu ', ' geta ', ' egziabiher ', ' igziabiher ', ' dingil ', ' kidusan ', ' inat ', ' amlak ']
    oromo_indicators = [' waaqayyoo ', ' gooftaa ', ' faaruu ', ' isaa ', ' koo ', ' kee ', ' nuuf ', ' sanaa ', ' nagaa ', ' garuu ', ' kana ']

    a_count = sum(text_lower.count(ind) for ind in amharic_indicators)
    o_count = sum(text_lower.count(ind) for ind in oromo_indicators)

    # Some fallback logic
    if a_count > o_count:
        return "Amharic"
    elif o_count > a_count:
        return "Afaan Oromo"
    
    if amharic_score > 2:
        return "Amharic"
    else:
        return "Afaan Oromo"

def main():
    mezmurs = []
    
    # Use regex to find mezmur headers, like "1.ARGADHEEN JIRA!!!" or "145 .ERGAAMOON SAMII"
    pattern = re.compile(r'^\s*(\d+)\s*\.\s*(.+?)(?:!!!)?\s*$', re.MULTILINE)
    
    matches = list(pattern.finditer(raw_text))
    
    for i in range(len(matches)):
        match = matches[i]
        num = int(match.group(1))
        title = match.group(2).strip()
        # strip exclamation marks from title if any remain
        title = re.sub(r'!+$', '', title).strip()
        
        start_idx = match.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(raw_text)
        
        content = raw_text[start_idx:end_idx].strip()
        
        # fix the title casing (e.g. ARGADHEEN JIRA -> Argadheen Jira)
        title = title.title()
        
        lang = guess_language(title + " " + content)
        
        mezmurs.append({
            'original_num': num,
            'title': title,
            'language': lang,
            'content': content
        })

    # Output stats
    print(f"Found {len(mezmurs)} mezmurs.")
    if len(mezmurs) > 0:
        print("Sorting...")
    
    # Sort: Oromo first, then Amharic. Then by title A-Z
    def sort_key(m):
        lang_order = 0 if m['language'] == 'Afaan Oromo' else 1
        return (lang_order, m['title'].lower())
        
    mezmurs.sort(key=sort_key)
    
    # Generate Dart code
    dart_code = "import '../models/mezmur.dart';\n\n"
    dart_code += "final List<Mezmur> mezmurs = [\n"
    
    for idx, mezmur in enumerate(mezmurs, 1):
        content_escaped = mezmur['content'].replace('\\', '\\\\').replace('$', '\\$').replace('\'', '\\\'')
        title_escaped = mezmur['title'].replace('\\', '\\\\').replace('$', '\\$').replace('\'', '\\\'')
        
        dart_code += f"  Mezmur(\n"
        dart_code += f"    id: {idx},\n"
        dart_code += f"    title: '{title_escaped}',\n"
        dart_code += f"    language: '{mezmur['language']}',\n"
        dart_code += f"    content: '''{content_escaped}''',\n"
        dart_code += f"  ),\n"
        
    dart_code += "];\n"
    
    with open(r'c:\Users\danie\.gemini\antigravity\scratch\mezmur_app\lib\data\mezmur_data.dart', 'w', encoding='utf-8') as f:
        f.write(dart_code)
        
    print("Successfully wrote lib/data/mezmur_data.dart")
    
if __name__ == '__main__':
    main()
