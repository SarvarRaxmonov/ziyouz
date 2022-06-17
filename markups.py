
from os import name
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, callback_game, inline_keyboard
from aiohttp.helpers import parse_mimetype
from attr import resolve_types

btnprofile = KeyboardButton(' profil ')
profilekey = ReplyKeyboardMarkup(resize_keyboard= True).add(btnprofile)

btnurchannel = InlineKeyboardButton(text='🕋  1-kanal  🕋', url='https://t.me/ilmziyomaskani')
btnurchannel2 = InlineKeyboardButton(text='🕋  2-kanal  🕋', url='https://t.me/elyorbekerkinbek')
btndonesub = InlineKeyboardButton(text='A\'zo buldim 🔴', callback_data="subchanneldone")

checksubmenu = InlineKeyboardMarkup(row_width=1)
checksubmenu.insert(btnurchannel)
checksubmenu.insert(btnurchannel2)
checksubmenu.insert(btndonesub)


cd = ' <b>📜 Surani tanlang</b>  \n  \n <b>1.</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ) \n <b>2.</b> Al-Baqara (سُورَةُ البَقَرَةِ) \n <b>3.</b> Aal-i-Imraan (سُورَةُ آلِ عِمۡرَانَ) \n <b>4.</b> An-Nisaa (سُورَةُ النِّسَاءِ) \n <b>5.</b> Al-Maaida (سُورَةُ المَائـِدَةِ) \n <b>6.</b> Al-An\'aam (سُورَةُ الأَنۡعَامِ) \n <b>7.</b> Al-A\'raaf (سُورَةُ الأَعۡرَافِ) \n <b>8.</b> Al-Anfaal (سُورَةُ الأَنفَالِ) \n <b>9.</b> At-Tawba (سُورَةُ التَّوۡبَةِ) \n <b>10.</b> Yunus (سُورَةُ يُونُسَ) \n <b>11.</b> Hud (سُورَةُ هُودٍ) \n <b>12.</b> Yusuf (سُورَةُ يُوسُفَ) \n <b>13.</b> Ar-Ra\'d (سُورَةُ الرَّعۡدِ) \n <b>14.</b> Ibrahim (سُورَةُ إِبۡرَاهِيمَ) \n <b>15.</b> Al-Hijr (سُورَةُ الحِجۡرِ) \n <b>16.</b> An-Nahl (سُورَةُ النَّحۡلِ) \n <b>17.</b> Al-Israa (سُورَةُ الإِسۡرَاءِ) \n <b>18.</b> Al-Kahf (سُورَةُ الكَهۡفِ) \n <b>19.</b> Maryam (سُورَةُ مَرۡيَمَ) \n <b>20.</b> Taa-Haa (سُورَةُ طه) \n <b>21.</b> Al-Anbiyaa (سُورَةُ الأَنبِيَاءِ) \n <b>22.</b> Al-Hajj (سُورَةُ الحَجِّ) \n <b>23.</b> Al-Muminoon (سُورَةُ المُؤۡمِنُونَ) \n <b>24.</b> An-Noor (سُورَةُ النُّورِ) \n <b>25.</b> Al-Furqaan (سُورَةُ الفُرۡقَانِ) \n <b>26.</b> Ash-Shu\'araa (سُورَةُ الشُّعَرَاءِ) \n <b>27.</b> An-Naml (سُورَةُ النَّمۡلِ) \n <b>28.</b> Al-Qasas (سُورَةُ القَصَصِ) \n <b>29.</b> Al-Ankaboot (سُورَةُ العَنكَبُوتِ) \n <b>30.</b> Ar-Room (سُورَةُ الرُّومِ) \n \n  <b>Hamma Audiolar uchun 📻</b> \n <b> Qorilar ro\'yxati uchun 🗒 </b>'  
cd3 = ' <b>📜 Surani tanlang</b>  \n \n <b>31.</b> Luqman (سُورَةُ لُقۡمَانَ) \n <b>32.</b> As-Sajda (سُورَةُ السَّجۡدَةِ) \n <b>33.</b> Al-Ahzaab (سُورَةُ الأَحۡزَابِ) \n <b>34.</b> Saba (سُورَةُ سَبَإٍ) \n <b>35.</b> Faatir (سُورَةُ فَاطِرٍ) \n <b>36.</b> Yaseen (سُورَةُ يسٓ) \n <b>37.</b> As-Saaffaat (سُورَةُ الصَّافَّاتِ) \n <b>38.</b> Saad (سُورَةُ صٓ) \n <b>39.</b> Az-Zumar (سُورَةُ الزُّمَرِ) \n <b>40.</b> Ghafir (سُورَةُ غَافِرٍ) \n <b>41.</b> Fussilat (سُورَةُ فُصِّلَتۡ) \n <b>42.</b> Ash-Shura (سُورَةُ الشُّورَىٰ) \n <b>43.</b> Az-Zukhruf (سُورَةُ الزُّخۡرُفِ) \n <b>44.</b> Ad-Dukhaan (سُورَةُ الدُّخَانِ) \n <b>45.</b> Al-Jaathiya (سُورَةُ الجَاثِيَةِ) \n <b>46.</b> Al-Ahqaf (سُورَةُ الأَحۡقَافِ) \n <b>47.</b> Muhammad (سُورَةُ مُحَمَّدٍ) \n <b>48.</b> Al-Fath (سُورَةُ الفَتۡحِ) \n <b>49.</b> Al-Hujuraat (سُورَةُ الحُجُرَاتِ) \n <b>50.</b> Qaaf (سُورَةُ قٓ) \n <b>51.</b> Adh-Dhaariyat (سُورَةُ الذَّارِيَاتِ) \n <b>52.</b> At-Tur (سُورَةُ الطُّورِ) \n <b>53.</b> An-Najm (سُورَةُ النَّجۡمِ) \n <b>54.</b> Al-Qamar (سُورَةُ القَمَرِ) \n <b>55.</b> Ar-Rahmaan (سُورَةُ الرَّحۡمَٰن) \n <b>56.</b> Al-Waaqia (سُورَةُ الوَاقِعَةِ) \n <b>57.</b> Al-Hadid (سُورَةُ الحَدِيدِ) \n <b>58.</b> Al-Mujaadila (سُورَةُ المُجَادلَةِ) \n <b>59.</b> Al-Hashr (سُورَةُ الحَشۡرِ) \n <b>60.</b> Al-Mumtahana (سُورَةُ المُمۡتَحنَةِ) \n \n  <b>Hamma Audiolar uchun 📻</b> \n <b> Qorilar ro\'yxati uchun 🗒 </b>'

cd5 = '<b>📜 Surani tanlang</b>  \n \n <b>61.</b> As-Saff (سُورَةُ الصَّفِّ) \n <b>62.</b> Al-Jumu\'a (سُورَةُ الجُمُعَةِ) \n <b>63.</b> Al-Munaafiqoon (سُورَةُ المُنَافِقُونَ) \n <b>64.</b> At-Taghaabun (سُورَةُ التَّغَابُنِ) \n <b>65.</b> At-Talaaq (سُورَةُ الطَّلَاقِ) \n <b>66.</b> At-Tahrim (سُورَةُ التَّحۡرِيمِ) \n <b>67.</b> Al-Mulk (سُورَةُ المُلۡكِ) \n <b>68.</b> Al-Qalam (سُورَةُ القَلَمِ) \n <b>69.</b> Al-Haaqqa (سُورَةُ الحَاقَّةِ) \n <b>70.</b> Al-Ma\'aarij (سُورَةُ المَعَارِجِ) \n <b>71.</b> Nooh (سُورَةُ نُوحٍ) \n <b>72.</b> Al-Jinn (سُورَةُ الجِنِّ) \n <b>73.</b> Al-Muzzammil (سُورَةُ المُزَّمِّلِ) \n <b>74.</b> Al-Muddaththir (سُورَةُ المُدَّثِّرِ) \n <b>75.</b> Al-Qiyaama (سُورَةُ القِيَامَةِ) \n <b>76.</b> Al-Insaan (سُورَةُ الإِنسَانِ) \n <b>77.</b> Al-Mursalaat (سُورَةُ المُرۡسَلَاتِ) \n <b>78.</b> An-Naba (سُورَةُ النَّبَإِ) \n <b>79.</b> An-Naazi\'aat (سُورَةُ النَّازِعَاتِ) \n <b>80.</b> Abasa (سُورَةُ عَبَسَ) \n <b>81.</b> At-Takwir (سُورَةُ التَّكۡوِيرِ) \n <b>82.</b> Al-Infitaar (سُورَةُ الانفِطَارِ) \n <b>83.</b> Al-Mutaffifin (سُورَةُ المُطَفِّفِينَ) \n <b>84.</b> Al-Inshiqaaq (سُورَةُ الانشِقَاقِ) \n <b>85.</b> Al-Burooj (سُورَةُ البُرُوجِ) \n <b>86.</b> At-Taariq (سُورَةُ الطَّارِقِ) \n <b>87.</b> Al-A\'laa (سُورَةُ الأَعۡلَىٰ) \n <b>88.</b> Al-Ghaashiya (سُورَةُ الغَاشِيَةِ) \n <b>89.</b> Al-Fajr (سُورَةُ الفَجۡرِ) \n <b>90.</b> Al-Balad (سُورَةُ البَلَدِ) \n \n  <b>Hamma Audiolar uchun 📻</b> \n <b> Qorilar ro\'yxati uchun 🗒 </b>'

cd7 = ' <b>📜 Surani tanlang</b>  \n \n <b>91.</b> Ash-Shams (سُورَةُ الشَّمۡسِ) \n <b>92.</b> Al-Lail (سُورَةُ اللَّيۡلِ) \n <b>93.</b> Ad-Dhuhaa (سُورَةُ الضُّحَىٰ) \n <b>94.</b> Ash-Sharh (سُورَةُ الشَّرۡحِ) \n <b>95.</b> At-Tin (سُورَةُ التِّينِ) \n <b>96.</b> Al-Alaq (سُورَةُ العَلَقِ) \n <b>97.</b> Al-Qadr (سُورَةُ القَدۡرِ) \n <b>98.</b> Al-Bayyina (سُورَةُ البَيِّنَةِ) \n <b>99.</b> Az-Zalzala (سُورَةُ الزَّلۡزَلَةِ) \n <b>100.</b> Al-Aadiyaat (سُورَةُ العَادِيَاتِ) \n <b>101.</b> Al-Qaari\'a (سُورَةُ القَارِعَةِ) \n <b>102.</b> At-Takaathur (سُورَةُ التَّكَاثُرِ) \n <b>103.</b> Al-Asr (سُورَةُ العَصۡرِ) \n <b>104.</b> Al-Humaza (سُورَةُ الهُمَزَةِ) \n <b>105.</b> Al-Fil (سُورَةُ الفِيلِ) \n <b>106.</b> Quraish (سُورَةُ قُرَيۡشٍ) \n <b>107.</b> Al-Maa\'un (سُورَةُ المَاعُونِ) \n <b>108.</b> Al-Kawthar (سُورَةُ الكَوۡثَرِ) \n <b>109.</b> Al-Kaafiroon (سُورَةُ الكَافِرُونَ) \n <b>110.</b> An-Nasr (سُورَةُ النَّصۡرِ) \n <b>111.</b> Al-Masad (سُورَةُ المَسَدِ) \n <b>112.</b> Al-Ikhlaas (سُورَةُ الإِخۡلَاصِ) \n <b>113.</b> Al-Falaq (سُورَةُ الفَلَقِ) \n <b>114.</b> An-Naas (سُورَةُ النَّاسِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'

qorilist =f' <b>📜 Qorini tanlang</b>  \n  \n <b>1.</b> Mishary bin Rashed Alafasy \n <b>2.</b> Abdul Rahman Al-Sudais \n <b>3.</b> Saud Al-Shuraim \n <b>4.</b> Saad Al-Ghamidi \n <b>5</b> Bandar Bin Abdulaziz Baleela \n <b>6.</b> Idris Akbar \n <b>7.</b> Yasser Al-Dosari \n <b>8.</b> Maher Al-Mueaqly \n <b>9.</b> Abdullah Awad Al-Juhany \n <b>10.</b> Abdul Basit Abdessamad \n <b>11.</b> Zaki Daghistani \n <b>12.</b> Sahl Yassin \n <b>13.</b> Mohammed Ayyub \n <b>14.</b> Raad Al-Kurdi \n <b>15.</b> Abdulrashed Soufi \n \n'



btnmain = InlineKeyboardButton('Quron 🎧')
btnmain2 = InlineKeyboardButton('Bot 📜')
btnmain3 = InlineKeyboardButton('Namoz ☪️')
btnmain4 = InlineKeyboardButton('Multifilim 📺')
btnmain5 = InlineKeyboardButton('Kitobxona 🏛')
btnmain6 = InlineKeyboardButton('Wikipedia 📰',callback_data="wiki")

wikiorqaga = InlineKeyboardButton(text='Wikipediaga 🔴', url='https://t.me/Wiki_ziyo_bot')
wikiorqagan = InlineKeyboardMarkup(resize_keyboard=True, row_width=3).add(wikiorqaga)
from datetime import datetime
import jsonuz as jsuz
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

btnorder = InlineKeyboardButton(datetime.now().strftime("%H:%M:%S"),'boshqa')

sainmenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnmain, btnmain2, btnmain3,btnmain4,btnmain5,btnmain6)
orqagaa = ReplyKeyboardMarkup(resize_keyboard=True).add(btnmain, btnmain2, btnmain3,btnmain4,btnmain5,btnmain6)
orqagaall = InlineKeyboardButton('Menu 📜',callback_data='orqagaall')
orqqagaqori = InlineKeyboardMarkup(resize_keyboard=True)
orqaga = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga')
keyingi = InlineKeyboardButton('Keyingi ➡️', callback_data='keyingi')
keyingi2 = InlineKeyboardButton('Keyingi ➡️', callback_data='keyingi2')
keyingi3 = InlineKeyboardButton('Keyingi ➡️', callback_data='keyingi3')
orqaga1 = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga1')
orqaga2 = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga2')
orqaga3 = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga3')
sura1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura2 = InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura3 = InlineKeyboardMarkup(resize_keyboard=True, row_width=5) 
sura4 = InlineKeyboardMarkup(resize_keyboard=True, row_width=7)

#birinchi qori
sura5 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura6 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura7 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura8 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#ikinchi qori
sura9 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura10 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura11 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura12 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#uchinchi qori
sura13 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura14 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura15 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura16 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#4 chi qori
sura17 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura18 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura19 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura20 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#5 chi qori
sura21 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura22 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura23 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura24 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#6 qori
sura25 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura26 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura27 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura28 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#7 qori
sura29 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura30 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura31 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura32 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#9 qori
sura33 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura34 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura35 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura36 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#10 chi qori
sura37 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura38 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura39 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura40 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#11 chi qori
sura41 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura42 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura43 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura44 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#12 chi qori
sura45 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura46 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura47 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura48 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#13 chi qori
sura49 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura50 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura51 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura52 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#14 chi qori
sura53 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura54 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura55 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura56 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#15 chi qori
sura57 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura58 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura59 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
sura60 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=6)


qorilists = InlineKeyboardMarkup(resize_keyboard=True, row_width=4)
 
hammadio1 = InlineKeyboardButton('📻', callback_data='hm1')
hammadio2 = InlineKeyboardButton('📻', callback_data='hm2')
hammadio3 = InlineKeyboardButton('📻', callback_data='hm3')
hammadio4 = InlineKeyboardButton('📻', callback_data='hm4')

for c in range(1,115):
      
  
    if c < 31:
        
              
               sura1.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
               sura5.insert(InlineKeyboardButton(text=c, callback_data=f"sura4{c}"));
               sura9.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}"));
               sura13.insert(InlineKeyboardButton(text=c, callback_data=f"sura6{c}"));
               sura17.insert(InlineKeyboardButton(text=c, callback_data=f"sura7{c}"));
               sura21.insert(InlineKeyboardButton(text=c, callback_data=f"sura8{c}"));
               sura25.insert(InlineKeyboardButton(text=c, callback_data=f"sura9{c}"));
               sura29.insert(InlineKeyboardButton(text=c, callback_data=f"sura10{c}"));
               sura33.insert(InlineKeyboardButton(text=c, callback_data=f"sura11{c}"));
               sura37.insert(InlineKeyboardButton(text=c, callback_data=f"sura12{c}"));
               sura41.insert(InlineKeyboardButton(text=c, callback_data=f"sura13{c}"));
               sura45.insert(InlineKeyboardButton(text=c, callback_data=f"sura14{c}"));
               
               sura49.insert(InlineKeyboardButton(text=c, callback_data=f"sura15{c}"));        
               sura53.insert(InlineKeyboardButton(text=c, callback_data=f"sura16{c}"));
               sura57.insert(InlineKeyboardButton(text=c, callback_data=f"sura17{c}"));          
               

    if c > 30:
         if c < 61:
              sura2.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
              sura6.insert(InlineKeyboardButton(text=c, callback_data=f"sura4{c}"));
              sura10.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}"));
              sura14.insert(InlineKeyboardButton(text=c, callback_data=f"sura6{c}"));
              sura18.insert(InlineKeyboardButton(text=c, callback_data=f"sura7{c}"));
              sura22.insert(InlineKeyboardButton(text=c, callback_data=f"sura8{c}"));
              
               
              sura26.insert(InlineKeyboardButton(text=c, callback_data=f"sura9{c}"));
              sura30.insert(InlineKeyboardButton(text=c, callback_data=f"sura10{c}"));
              sura34.insert(InlineKeyboardButton(text=c, callback_data=f"sura11{c}"));
              sura38.insert(InlineKeyboardButton(text=c, callback_data=f"sura12{c}"));
              sura42.insert(InlineKeyboardButton(text=c, callback_data=f"sura13{c}"));
              sura46.insert(InlineKeyboardButton(text=c, callback_data=f"sura14{c}"));

              sura50.insert(InlineKeyboardButton(text=c, callback_data=f"sura15{c}"));
              sura54.insert(InlineKeyboardButton(text=c, callback_data=f"sura16{c}"));
              sura58.insert(InlineKeyboardButton(text=c, callback_data=f"sura17{c}")); 
                    
   
    if c > 60:
         if c < 91:
              sura3.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
              sura7.insert(InlineKeyboardMarkup(text=c, callback_data=f"sura4{c}"));
              sura11.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}")); 
              sura15.insert(InlineKeyboardButton(text=c, callback_data=f"sura6{c}"));
              sura19.insert(InlineKeyboardButton(text=c, callback_data=f"sura7{c}"));
              sura23.insert(InlineKeyboardButton(text=c, callback_data=f"sura8{c}"));
              
               
              sura27.insert(InlineKeyboardButton(text=c, callback_data=f"sura9{c}"));
              sura31.insert(InlineKeyboardButton(text=c, callback_data=f"sura10{c}"));
              sura35.insert(InlineKeyboardButton(text=c, callback_data=f"sura11{c}"));
              sura39.insert(InlineKeyboardButton(text=c, callback_data=f"sura12{c}"));
              sura43.insert(InlineKeyboardButton(text=c, callback_data=f"sura13{c}"));
              sura47.insert(InlineKeyboardButton(text=c, callback_data=f"sura14{c}"));
              
              
              sura51.insert(InlineKeyboardButton(text=c, callback_data=f"sura15{c}"));
              sura55.insert(InlineKeyboardButton(text=c, callback_data=f"sura16{c}"));
              sura59.insert(InlineKeyboardButton(text=c, callback_data=f"sura17{c}")); 
    if c > 90:
         if c < 115:
              sura4.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
              sura8.insert(InlineKeyboardButton(text=c, callback_data=f"sura4{c}"));
              sura12.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}"));
              sura16.insert(InlineKeyboardButton(text=c, callback_data=f"sura6{c}"));
              sura20.insert(InlineKeyboardButton(text=c, callback_data=f"sura7{c}"));
              sura24.insert(InlineKeyboardButton(text=c, callback_data=f"sura8{c}"));
              
               
              sura28.insert(InlineKeyboardButton(text=c, callback_data=f"sura9{c}"));
              sura32.insert(InlineKeyboardButton(text=c, callback_data=f"sura10{c}"));
              sura36.insert(InlineKeyboardButton(text=c, callback_data=f"sura11{c}")); 
              sura40.insert(InlineKeyboardButton(text=c, callback_data=f"sura12{c}"));
              sura44.insert(InlineKeyboardButton(text=c, callback_data=f"sura13{c}"));
              sura48.insert(InlineKeyboardButton(text=c, callback_data=f"sura14{c}"));
              
              
              sura52.insert(InlineKeyboardButton(text=c, callback_data=f"sura15{c}"));
              sura56.insert(InlineKeyboardButton(text=c, callback_data=f"sura16{c}"));
              sura60.insert(InlineKeyboardButton(text=c, callback_data=f"sura17{c}")); 
#qorilar listi
    if c < 16:
             qorilists.insert(InlineKeyboardButton(text=c, callback_data=f"qori{c}"))
import kutubxona 
uzv = {sura5:{'reply':sura6,'cd':cd3,'t':'5'}, sura6:{'reply':sura7,'cd':cd5,'t':'6'}, sura7:{'reply':sura8,'cd':cd7,'t':'7'}, 
       sura9:{'reply':sura10,'cd':cd3,'t':'8'}, sura10:{'reply':sura11,'cd':cd5,'t':'9'}, sura11:{'reply':sura12,'cd':cd7,'t':'10'},sura13:{'reply':sura14,'cd':cd3,'t':'11'},sura14:{'reply':sura15,'cd':cd5,'t':'12'},sura15:{'reply':sura16,'cd':cd7,'t':'13'}
       ,sura17:{'reply':sura18,'cd':cd3,'t':'14'}, sura18:{'reply':sura19,'cd':cd5,'t':'15'},sura19:{'reply':sura20,'cd':cd7,'t':'16'}, #sura5 
       sura21:{'reply':sura22,'cd':cd3,'t':'17'},sura22:{'reply':sura23,'cd':cd5,'t':'18'},sura23:{'reply':sura24,'cd':cd7,'t':'19'}, 
       
       #sura6
       sura25:{'reply':sura26,'cd':cd3,'t':'20'},sura26:{'reply':sura27,'cd':cd5,'t':'21'},sura27:{'reply':sura28,'cd':cd7,'t':'22'}, 
       
       #sura7 
       sura29:{'reply':sura30,'cd':cd3,'t':'23'},sura30:{'reply':sura31,'cd':cd5,'t':'24'},sura31:{'reply':sura32,'cd':cd7,'t':'25'}, 
       #sura8 
       sura33:{'reply':sura34,'cd':cd3,'t':'26'},sura34:{'reply':sura35,'cd':cd5,'t':'27'},sura35:{'reply':sura36,'cd':cd7,'t':'28'}, 
       #sura9 
       sura37:{'reply':sura38,'cd':cd3,'t':'29'},sura38:{'reply':sura39,'cd':cd5,'t':'30'},sura39:{'reply':sura40,'cd':cd7,'t':'31'}, 
       #sura10 
       sura41:{'reply':sura42,'cd':cd3,'t':'32'},sura42:{'reply':sura43,'cd':cd5,'t':'33'},sura43:{'reply':sura44,'cd':cd7,'t':'34'}, 
       #sura11 
       sura45:{'reply':sura46,'cd':cd3,'t':'35'},sura46:{'reply':sura47,'cd':cd5,'t':'36'},sura47:{'reply':sura48,'cd':cd7,'t':'37'}, 
       #sura12 
       sura49:{'reply':sura50,'cd':cd3,'t':'38'},sura50:{'reply':sura51,'cd':cd5,'t':'39'},sura51:{'reply':sura52,'cd':cd7,'t':'40'}, 
       #sura13 
       sura53:{'reply':sura54,'cd':cd3,'t':'41'},sura54:{'reply':sura55,'cd':cd5,'t':'42'},sura55:{'reply':sura56,'cd':cd7,'t':'43'}, 
       #sura14 
       sura57:{'reply':sura58,'cd':cd3,'t':'44'},sura58:{'reply':sura59,'cd':cd5,'t':'45'},sura59:{'reply':sura60,'cd':cd7,'t':'46'}, 
       #sura15 
       kutubxona.kitob1:{'reply':kutubxona.kitob2, 'cd':kutubxona.cdb2, 't':'s47'},
   
       }  

uzv2 = {sura5:{'reply':qorilists, 'cd':qorilist,'t':'5'},sura6:{'reply':sura5,'cd':cd,'t':'6'}, sura7:{'reply':sura6,'cd':cd3,'t':'7'},  
       sura8:{'reply':sura7,'cd':cd7,'t':'8'}, sura9:{'reply':qorilists,'cd':qorilist,'t':'9'}, sura10:{'reply':sura9,'cd':cd,'t':'10'}, sura11:{'reply':sura10,'cd':cd3,'t':'11'},sura12:{'reply':sura11,'cd':cd5,'t':'12'},sura13:{'reply':qorilists,'cd':qorilist,'t':'13'},sura14:{'reply':sura13,'cd':cd,'t':'14'},sura15:{'reply':sura14,'cd':cd3,'t':'15'},
       sura16:{'reply':sura15,'cd':cd5,'t':'16'},sura17:{'reply':qorilists,'cd':qorilist,'t':'17'},sura18:{'reply':sura17,'cd':cd,'t':'18'},sura19:{'reply':sura18,'cd':cd3,'t':'19'},sura20:{'reply':sura19,'cd':cd5,'t':'20'}, #sura5
       sura21:{'reply':qorilists,'cd':qorilist,'t':'21'}, sura22:{'reply':sura21,'cd':cd,'t':'22'}, sura23:{'reply':sura22,'cd':cd3,'t':'23'}, sura24:{'reply':sura23,'cd':cd5,'t':'24'},           
       
       #sura6
       sura25:{'reply':qorilists,'cd':qorilist,'t':'25'},sura26:{'reply':sura25,'cd':cd,'t':'26'},sura27:{'reply':sura26,'cd':cd3,'t':'27'}, 
       sura28:{'reply':sura27,'cd':cd5, 't':'28'},
       #sura7 
       sura29:{'reply':qorilists,'cd':qorilist,'t':'29'},sura30:{'reply':sura29,'cd':cd,'t':'30'},sura31:{'reply':sura30,'cd':cd3,'t':'31'},
       sura32:{'reply':sura31,'cd':cd5, 't':'32'},
       #sura8 
       sura33:{'reply':qorilists,'cd':qorilist,'t':'33'},sura34:{'reply':sura33,'cd':cd,'t':'34'},sura35:{'reply':sura34,'cd':cd3,'t':'35'}, 
       sura36:{'reply':sura35,'cd':cd5, 't':'36'}, 
       #sura9 
       sura37:{'reply':qorilists,'cd':qorilist,'t':'37'},sura38:{'reply':sura37,'cd':cd,'t':'38'},sura39:{'reply':sura38,'cd':cd3,'t':'39'}, 
              sura40:{'reply':sura39,'cd':cd5, 't':'40'},
       #sura10 
       sura41:{'reply':qorilists,'cd':qorilist,'t':'41'},sura42:{'reply':sura41,'cd':cd,'t':'42'},sura43:{'reply':sura42,'cd':cd3,'t':'43'},
              sura44:{'reply':sura43,'cd':cd5, 't':'44'}, 
       #sura11 
       sura45:{'reply':qorilists,'cd':qorilist,'t':'45'},sura46:{'reply':sura45,'cd':cd,'t':'46'},sura47:{'reply':sura46,'cd':cd3,'t':'47'}, 
              sura48:{'reply':sura47,'cd':cd5, 't':'48'},
       #sura12 
       sura49:{'reply':qorilists,'cd':qorilist,'t':'49'},sura50:{'reply':sura49,'cd':cd,'t':'50'},sura51:{'reply':sura50,'cd':cd3,'t':'51'},
              sura52:{'reply':sura51,'cd':cd5, 't':'52'}, 
       #sura13 
       sura53:{'reply':qorilists,'cd':qorilist,'t':'53'},sura54:{'reply':sura53,'cd':cd,'t':'54'},sura55:{'reply':sura54,'cd':cd3,'t':'55'},
              sura56:{'reply':sura55,'cd':cd5, 't':'56'}, 
       #sura14 
       sura57:{'reply':qorilists,'cd':qorilist,'t':'57'},sura58:{'reply':sura57,'cd':cd,'t':'58'},sura59:{'reply':sura58,'cd':cd3,'t':'59'},
              sura60:{'reply':sura59,'cd':cd5, 't':'60'}, 
       #sura15 
   
       #kutubxona uchun    
        kutubxona.kitob2:{'reply':kutubxona.kitob1, 'cd':kutubxona.cdb, 't':'o48'},
         kutubxona.kitob1:{'reply':kutubxona.kitob1, 'cd':kutubxona.cdb, 't':'o47'},
   
        
   
       }  
  
for i,v in uzv2.items():
           d = v['t']
           
           i.insert(InlineKeyboardButton(text='⬅️', callback_data=f"ortga{d}"));
           if d[0] !='o':
                   i.insert(InlineKeyboardButton(text='📻', callback_data=f"hm{d}"))
           
for i,v in uzv.items():
       
       d = v['t']
       if d[0] !='s': 
                  i.insert(InlineKeyboardButton(text='🗒',callback_data='orqagaqori'))
       i.insert(InlineKeyboardButton(text='➡️', callback_data=f'keyingi{d}')); 

menubu = InlineKeyboardButton(text='🗒 Menu Qorilar',callback_data='orqagaqori')   
orqqagaqori.insert(menubu)     
qolibketgan = [sura1,sura2,sura3,sura4]

sura1.insert(orqaga)
sura1.insert(hammadio1)
sura1.insert(keyingi)
sura2.insert(orqaga1)
sura2.insert(hammadio2)
sura2.insert(keyingi2)
sura3.insert(orqaga2)
sura3.insert(hammadio3)
sura3.insert(keyingi3)
sura4.insert(hammadio4)
sura4.insert(orqaga3)
for i in qolibketgan:
     i.insert(InlineKeyboardButton(text='🗒',callback_data='orqagaqori'))
btninfo = KeyboardButton(' quron')

btnerkak = KeyboardButton('Erkaklarga 👨‍🦰')
btnayol = KeyboardButton('Ayollarga 👩‍🦰')
orqaga = KeyboardButton('Menu 📜')
orqagaerkaklar = KeyboardButton('Menu 📜')
orqagaayollar= KeyboardButton('Menu 📜')


namozbulimi = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnayol, btnerkak, orqaga)


namozbulimia = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


namozbulimie = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)



       
namozlist = ['Bomdod 🌃','Peshin 🌇','Asr 🏙','Shom 🌉','Xufton 🌌','Menu 📜']
for i in namozlist:
    namozbulimie.insert(KeyboardButton(text=i, one_time_keyboard=True))
    
    
    
namozlist2 = ['Bomdod 🌃ㅤ','Peshin 🌇ㅤ','Asr 🏙ㅤ','Shom 🌉ㅤ','Xufton 🌌ㅤ','Menu 📜']
    
for n in namozlist2:
     namozbulimia.insert(KeyboardButton(text=n))
    
     
     
     
multi = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)

multilist = ['Menu 📜','Qur\'onda zikri kelgan ajoyibotlar 🕋','Qur\'onda zikri kelgan insonlar qissasi 🏔','Imom Al-buxoriy ⚜️','Payg\'ambarlar Tarixi ☪️','Imom Termiziy 🕯']
for n in multilist:
    multi.insert(KeyboardButton(text=n))
    

pdf = KeyboardButton(text="Kitoblar 📚")
audio = KeyboardButton(text="Audio 🎧")
menukitobortga = KeyboardButton(text="Menu 📜")
menukitob = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(pdf,audio,menukitobortga)