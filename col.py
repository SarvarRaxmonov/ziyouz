


import logging
from typing import Literal
from aiogram import  Bot, Dispatcher, executor, types
from aiogram.types import audio, callback_game, message, message_entity, reply_keyboard, user
from aiogram.types import callback_query
from aiogram.types.callback_query import CallbackQuery
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from aiogram.utils import markdown
from aiohttp.client import _WSRequestContextManager, request
import kutubxona
TOKENn = '5065335871:AAECacrGIAWaYGvXkg_9yJYkt3z7aF0WKas'
logging.basicConfig(level=logging.INFO)
from aiogram.utils.markdown import hide_link, text
import asyncio
loop = asyncio.get_event_loop()
bot = Bot(token=TOKENn,loop=loop, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
CHANNEL_ID = '@sharqiy_turkiston'
CHANNEL_ID2 = '@uzbek_economis1'
import markups as nav
import jsonuz as jsuz
#code
cd = ' <b>📜 Surani tanlang</b>  \n  \n <b>1.</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ) \n <b>2.</b> Al-Baqara (سُورَةُ البَقَرَةِ) \n <b>3.</b> Aal-i-Imraan (سُورَةُ آلِ عِمۡرَانَ) \n <b>4.</b> An-Nisaa (سُورَةُ النِّسَاءِ) \n <b>5.</b> Al-Maaida (سُورَةُ المَائـِدَةِ) \n <b>6.</b> Al-An\'aam (سُورَةُ الأَنۡعَامِ) \n <b>7.</b> Al-A\'raaf (سُورَةُ الأَعۡرَافِ) \n <b>8.</b> Al-Anfaal (سُورَةُ الأَنفَالِ) \n <b>9.</b> At-Tawba (سُورَةُ التَّوۡبَةِ) \n <b>10.</b> Yunus (سُورَةُ يُونُسَ) \n <b>11.</b> Hud (سُورَةُ هُودٍ) \n <b>12.</b> Yusuf (سُورَةُ يُوسُفَ) \n <b>13.</b> Ar-Ra\'d (سُورَةُ الرَّعۡدِ) \n <b>14.</b> Ibrahim (سُورَةُ إِبۡرَاهِيمَ) \n <b>15.</b> Al-Hijr (سُورَةُ الحِجۡرِ) \n <b>16.</b> An-Nahl (سُورَةُ النَّحۡلِ) \n <b>17.</b> Al-Israa (سُورَةُ الإِسۡرَاءِ) \n <b>18.</b> Al-Kahf (سُورَةُ الكَهۡفِ) \n <b>19.</b> Maryam (سُورَةُ مَرۡيَمَ) \n <b>20.</b> Taa-Haa (سُورَةُ طه) \n <b>21.</b> Al-Anbiyaa (سُورَةُ الأَنبِيَاءِ) \n <b>22.</b> Al-Hajj (سُورَةُ الحَجِّ) \n <b>23.</b> Al-Muminoon (سُورَةُ المُؤۡمِنُونَ) \n <b>24.</b> An-Noor (سُورَةُ النُّورِ) \n <b>25.</b> Al-Furqaan (سُورَةُ الفُرۡقَانِ) \n <b>26.</b> Ash-Shu\'araa (سُورَةُ الشُّعَرَاءِ) \n <b>27.</b> An-Naml (سُورَةُ النَّمۡلِ) \n <b>28.</b> Al-Qasas (سُورَةُ القَصَصِ) \n <b>29.</b> Al-Ankaboot (سُورَةُ العَنكَبُوتِ) \n <b>30.</b> Ar-Room (سُورَةُ الرُّومِ) \n \n  <b>Hamma Audiolar uchun 📻</b> \n <b> Qorilar ro\'yxati uchun : 🗒 </b>'  
cd3 = ' <b>📜 Surani tanlang</b>  \n \n <b>31.</b> Luqman (سُورَةُ لُقۡمَانَ) \n <b>32.</b> As-Sajda (سُورَةُ السَّجۡدَةِ) \n <b>33.</b> Al-Ahzaab (سُورَةُ الأَحۡزَابِ) \n <b>34.</b> Saba (سُورَةُ سَبَإٍ) \n <b>35.</b> Faatir (سُورَةُ فَاطِرٍ) \n <b>36.</b> Yaseen (سُورَةُ يسٓ) \n <b>37.</b> As-Saaffaat (سُورَةُ الصَّافَّاتِ) \n <b>38.</b> Saad (سُورَةُ صٓ) \n <b>39.</b> Az-Zumar (سُورَةُ الزُّمَرِ) \n <b>40.</b> Ghafir (سُورَةُ غَافِرٍ) \n <b>41.</b> Fussilat (سُورَةُ فُصِّلَتۡ) \n <b>42.</b> Ash-Shura (سُورَةُ الشُّورَىٰ) \n <b>43.</b> Az-Zukhruf (سُورَةُ الزُّخۡرُفِ) \n <b>44.</b> Ad-Dukhaan (سُورَةُ الدُّخَانِ) \n <b>45.</b> Al-Jaathiya (سُورَةُ الجَاثِيَةِ) \n <b>46.</b> Al-Ahqaf (سُورَةُ الأَحۡقَافِ) \n <b>47.</b> Muhammad (سُورَةُ مُحَمَّدٍ) \n <b>48.</b> Al-Fath (سُورَةُ الفَتۡحِ) \n <b>49.</b> Al-Hujuraat (سُورَةُ الحُجُرَاتِ) \n <b>50.</b> Qaaf (سُورَةُ قٓ) \n <b>51.</b> Adh-Dhaariyat (سُورَةُ الذَّارِيَاتِ) \n <b>52.</b> At-Tur (سُورَةُ الطُّورِ) \n <b>53.</b> An-Najm (سُورَةُ النَّجۡمِ) \n <b>54.</b> Al-Qamar (سُورَةُ القَمَرِ) \n <b>55.</b> Ar-Rahmaan (سُورَةُ الرَّحۡمَٰن) \n <b>56.</b> Al-Waaqia (سُورَةُ الوَاقِعَةِ) \n <b>57.</b> Al-Hadid (سُورَةُ الحَدِيدِ) \n <b>58.</b> Al-Mujaadila (سُورَةُ المُجَادلَةِ) \n <b>59.</b> Al-Hashr (سُورَةُ الحَشۡرِ) \n <b>60.</b> Al-Mumtahana (سُورَةُ المُمۡتَحنَةِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'

cd5 = '<b>📜 Surani tanlang</b>  \n \n <b>61.</b> As-Saff (سُورَةُ الصَّفِّ) \n <b>62.</b> Al-Jumu\'a (سُورَةُ الجُمُعَةِ) \n <b>63.</b> Al-Munaafiqoon (سُورَةُ المُنَافِقُونَ) \n <b>64.</b> At-Taghaabun (سُورَةُ التَّغَابُنِ) \n <b>65.</b> At-Talaaq (سُورَةُ الطَّلَاقِ) \n <b>66.</b> At-Tahrim (سُورَةُ التَّحۡرِيمِ) \n <b>67.</b> Al-Mulk (سُورَةُ المُلۡكِ) \n <b>68.</b> Al-Qalam (سُورَةُ القَلَمِ) \n <b>69.</b> Al-Haaqqa (سُورَةُ الحَاقَّةِ) \n <b>70.</b> Al-Ma\'aarij (سُورَةُ المَعَارِجِ) \n <b>71.</b> Nooh (سُورَةُ نُوحٍ) \n <b>72.</b> Al-Jinn (سُورَةُ الجِنِّ) \n <b>73.</b> Al-Muzzammil (سُورَةُ المُزَّمِّلِ) \n <b>74.</b> Al-Muddaththir (سُورَةُ المُدَّثِّرِ) \n <b>75.</b> Al-Qiyaama (سُورَةُ القِيَامَةِ) \n <b>76.</b> Al-Insaan (سُورَةُ الإِنسَانِ) \n <b>77.</b> Al-Mursalaat (سُورَةُ المُرۡسَلَاتِ) \n <b>78.</b> An-Naba (سُورَةُ النَّبَإِ) \n <b>79.</b> An-Naazi\'aat (سُورَةُ النَّازِعَاتِ) \n <b>80.</b> Abasa (سُورَةُ عَبَسَ) \n <b>81.</b> At-Takwir (سُورَةُ التَّكۡوِيرِ) \n <b>82.</b> Al-Infitaar (سُورَةُ الانفِطَارِ) \n <b>83.</b> Al-Mutaffifin (سُورَةُ المُطَفِّفِينَ) \n <b>84.</b> Al-Inshiqaaq (سُورَةُ الانشِقَاقِ) \n <b>85.</b> Al-Burooj (سُورَةُ البُرُوجِ) \n <b>86.</b> At-Taariq (سُورَةُ الطَّارِقِ) \n <b>87.</b> Al-A\'laa (سُورَةُ الأَعۡلَىٰ) \n <b>88.</b> Al-Ghaashiya (سُورَةُ الغَاشِيَةِ) \n <b>89.</b> Al-Fajr (سُورَةُ الفَجۡرِ) \n <b>90.</b> Al-Balad (سُورَةُ البَلَدِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'

cd7 = ' <b>📜 Surani tanlang</b>  \n \n <b>91.</b> Ash-Shams (سُورَةُ الشَّمۡسِ) \n <b>92.</b> Al-Lail (سُورَةُ اللَّيۡلِ) \n <b>93.</b> Ad-Dhuhaa (سُورَةُ الضُّحَىٰ) \n <b>94.</b> Ash-Sharh (سُورَةُ الشَّرۡحِ) \n <b>95.</b> At-Tin (سُورَةُ التِّينِ) \n <b>96.</b> Al-Alaq (سُورَةُ العَلَقِ) \n <b>97.</b> Al-Qadr (سُورَةُ القَدۡرِ) \n <b>98.</b> Al-Bayyina (سُورَةُ البَيِّنَةِ) \n <b>99.</b> Az-Zalzala (سُورَةُ الزَّلۡزَلَةِ) \n <b>100.</b> Al-Aadiyaat (سُورَةُ العَادِيَاتِ) \n <b>101.</b> Al-Qaari\'a (سُورَةُ القَارِعَةِ) \n <b>102.</b> At-Takaathur (سُورَةُ التَّكَاثُرِ) \n <b>103.</b> Al-Asr (سُورَةُ العَصۡرِ) \n <b>104.</b> Al-Humaza (سُورَةُ الهُمَزَةِ) \n <b>105.</b> Al-Fil (سُورَةُ الفِيلِ) \n <b>106.</b> Quraish (سُورَةُ قُرَيۡشٍ) \n <b>107.</b> Al-Maa\'un (سُورَةُ المَاعُونِ) \n <b>108.</b> Al-Kawthar (سُورَةُ الكَوۡثَرِ) \n <b>109.</b> Al-Kaafiroon (سُورَةُ الكَافِرُونَ) \n <b>110.</b> An-Nasr (سُورَةُ النَّصۡرِ) \n <b>111.</b> Al-Masad (سُورَةُ المَسَدِ) \n <b>112.</b> Al-Ikhlaas (سُورَةُ الإِخۡلَاصِ) \n <b>113.</b> Al-Falaq (سُورَةُ الفَلَقِ) \n <b>114.</b> An-Naas (سُورَةُ النَّاسِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'
orqaga = '📜 Suralar ro\'yxatiga qaytish uchun orqagani bosing'
qorilist =f' <b>📜 Qorini tanlang</b>  \n  \n <b>1.</b> Mishary bin Rashed Alafasy \n <b>2.</b> Abdul Rahman Al-Sudais \n <b>3.</b> Saud Al-Shuraim \n <b>4.</b> Saad Al-Ghamidi \n <b>5</b> Bandar Bin Abdulaziz Baleela \n <b>6.</b> Idris Akbar \n <b>7.</b> Yasser Al-Dosari \n <b>8.</b> Maher Al-Mueaqly \n <b>9.</b> Abdullah Awad Al-Juhany \n <b>10.</b> Abdul Basit Abdessamad \n <b>11.</b> Zaki Daghistani \n <b>12.</b> Sahl Yassin \n <b>13.</b> Mohammed Ayyub \n <b>14.</b> Raad Al-Kurdi \n <b>15.</b> Abdulrashed Soufi \n \n'

# import requests

# url = "https://dailyprayer.abdulrcs.repl.co/api/jizzax"
# response = requests.get(url)
# data = response.json()
# print(data['city'])
# print(data['date'])
# for prayer in data["today"]:
#   print(prayer + ": " + data["today"][prayer])  



# url = "http://api.alquran.cloud/v1/edition?format=audio&language=fr&type=versebyverse"
# response = requests.get(url)
# data = response.json()
# print(data['data']) 

# for prayer in data["today"]:
#   print(prayer + ": " + data["today"][prayer])  





       

@dp.message_handler(commands=['star'])
async def start(message: types.Message):
     if message.chat.type == 'private': 
              
                     message.from_user.id = 761117518
                     
                     await bot.send_message(message.from_user.id , f" heloo {message.from_user.first_name}" , parse_mode='HTML' ,reply_markup=nav.qorila2)
              
              

linklar = '<b><a href="https://t.me/ilmziyomaskani"> Ilm - Ziyo maskani</a></b> \n \n <b>Саҳифаларимизга аъзо бўлинг:</b> \n <a href="https://www.facebook.com/ilmZiyoMaskani/">Facebook</a> : <a href="https://www.youtube.com/channel/UC8kKkNSXnafsOb0kb0hX5hw?sub_confirmation=1">Youtube</a> : <a href="https://www.instagram.com/ilmziyomaskani/">Instagram</a> : <a href="https://vm.tiktok.com/ZSxoUrLt/">\n Tiktok</a>'
linklar2 = '<b> @ilmziyomaskani </b> \n \n <b>Саҳифаларимизга аъзо бўлинг:</b> \n <a href="https://www.facebook.com/ilmZiyoMaskani/">Facebook</a> : <a href="https://www.youtube.com/channel/UC8kKkNSXnafsOb0kb0hX5hw?sub_confirmation=1">Youtube</a> : <a href="https://www.instagram.com/ilmziyomaskani/">Instagram</a> : <a href="https://vm.tiktok.com/ZSxoUrLt/">\n Tiktok</a>'

namoz = ['<b>Bomdod namozining</b> 2 rakat sunnati ','<b>Bomdod namozining</b> 2 rakat farzi','<b>Peshin namozining</b> 4 rakat sunnati ',
        '<b>Peshin namozining</b> 4 rakat farzi','<b>Peshin namozining</b> 2 rakat sunnati','<b>Asr namozining</b> 4 rakat farzi',
        '<b>Shom namozining</b> 3 rakat farzi','<b>Shom namozining</b> 2 rakat sunnati','<b>Xufton namozining</b> 4 rakat farzi ',
        '<b>Xufton namozining</b> 2 rakat sunati','<b>Vitr vojib namozining</b> 3 rakat ']
           





def check_sub_channel(chat_member):
    
    if chat_member['status'] != 'left':
        return True
    else:
        print('Notug\'ri kanalga obuna bulish')
        return False
        

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
           if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
               
               await bot.send_message(message.from_user.id, f'Assalomu alaykum <b>{message.from_user.first_name} \n Kanalarimizga obuna buling  🔴 </b>' , reply_markup=nav.checksubmenu)
           elif check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID2, user_id=message.from_user.id)):
               await bot.send_message(message.from_user.id, f'Kanallarga obuna buling 🔴⚠️ | \nkeyin /start qayta bosing' , reply_markup=nav.checksubmenu)
           else:
               await bot.send_message(message.from_user.id, 'Kanallarga obuna buling 🔴⚠️ | \nkeyin /start qayta bosing ', reply_markup=nav.checksubmenu)



@dp.callback_query_handler(text="subchanneldone")
async def subchanell(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)) & check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID2, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id,'😊 Raxmat foydalanishingiz mumkin | <b> agar muomo bulsa: /start ni  bosing </b> ', reply_markup=nav.sainmenu)
   
    
    else:
        await bot.send_message(message.from_user.id, 'Kanallarga obuna buling 🔴⚠️ | \nkeyin /start qayta bosing ', reply_markup=nav.checksubmenu)

nn = 'text'
@dp.callback_query_handler(text='orqaga')
async def  botquery(message: types.Message):
    
                if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)) & check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID2, user_id=message.from_user.id)):

                                await bot.delete_message(message.from_user.id,  message.message.message_id)
                                await bot.send_message(message.from_user.id, f'{qorilist}  O\'zingizga kerakli bo\'limni tanlang 🔽', reply_markup=nav.qorilists)

@dp.message_handler(text='Wikipedia 📰')
async def wiki(message: types.Message):
        
         
          if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)) & check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID2, user_id=message.from_user.id)):
              
                       await bot.send_message(message.from_user.id, f'Wikipedia bo\'limiga o\'ting ⤵️',reply_markup=nav.wikiorqagan )  

                                                                

@dp.callback_query_handler()
async def  botquery(callback_query_data: types.CallbackQuery):
        
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback_query_data.from_user.id)) & check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID2, user_id=callback_query_data.from_user.id)):
             
                if  callback_query_data.data == 'orqagaqori':
                        
                             await callback_query_data.message.edit_text(qorilist,reply_markup=nav.qorilists)
                for key,valu in jsuz.sura.items():
                        
                       
                         if  callback_query_data.data == f'sura3{key}':
                             g= valu['s1']
                             await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/b148uz/{g}')
                         if callback_query_data.data == f"sura4{key}":
                             g= valu['s2']
                             await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/MisharyRoshidQuran/{g}')
                         if callback_query_data.data == f"sura5{key}":
                             g= valu['s3']
                             await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/Sheikh_Abdul_Rahman_Al_Sudais/{g}')
                         if callback_query_data.data == f"sura6{key}":
                              g= valu['s4']
                              await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/shuraim1/{g}')
                         if callback_query_data.data == f"sura7{key}":
                              g= valu['s5']
                              await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/alquran30juzsaadalghamidi/{g}')
                         if callback_query_data.data == f"sura8{key}":
                              g= valu['s6']
                              await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/bandar_abdulaziz_balilah/{g}')
                         if callback_query_data.data == f"sura9{key}":
                              g= valu['s7']
                              await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/Idriss_Akbar/{g}')
                         if callback_query_data.data == f"sura10{key}":
                              g= valu['s8']
                              await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/yasseraldosari_mp3/{g}')
                         if callback_query_data.data == f"sura11{key}":
                              g= valu['s9']
                              await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/juhany_mp3/{g}')
                         if callback_query_data.data == f"sura12{key}":
                                  g= valu['s10']
                                  await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/madjmuah_1/{g}')
                         if callback_query_data.data == f"sura13{key}":
                                  g= valu['s11']
                                  await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/Zaki_Dagistan/{g}')
                         if callback_query_data.data == f"sura14{key}":
                                  g= valu['s12']
                                  await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/sahlyasin/{g}')
                         if callback_query_data.data == f"sura15{key}":
                                  g= valu['s13']
                                  await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/Muhammad_Ayyub1/{g}')
                         if callback_query_data.data == f"sura16{key}":
                                  g= valu['s14']
                                  await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/Raad_al_kurdi_mp3/{g}')
                         if callback_query_data.data == f"sura17{key}":  
                                  g= valu['s15']
                                  await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/alisufi30/{g}')
                for key,valu in jsuz.kitoblink.items():
                         if callback_query_data.data == f"kitob{key}":
                                  g= valu['b1']
                                  await bot.send_document(callback_query_data.from_user.id,caption='<b> Kanalimizga obuna buling : </b> @ilmziyomaskani', document=f'https://t.me/b148uz/{g}', )
     
                                    
                qorisura = {'1':{'r':nav.sura5, 'qori':'Mishary bin Rashed Alafasy'},'2':{'r':nav.sura9, 'qori':'Abdul Rahman Al-Sudais'},'3':{'r':nav.sura13, 'qori':' Saud Al-Shuraim '}, '4':{'r':nav.sura17, 'qori':'Saad Al-Ghamidi'},'5':{'r':nav.sura21, 'qori':'Bandar Bin Abdulaziz Baleela'},'6':{'r':nav.sura25, 'qori':' Idris Akbar '},
                            '7':{'r':nav.sura29, 'qori':'Yasser Al-Dosari'}, '8': {'r':nav.sura1,'qori':'Maher Al-Mueaqly'}, '9':{'r':nav.sura33, 'qori':' 9. Abdullah Awad Al-Juhany'}, '10':{'r':nav.sura37, 'qori':'Abdul Basit Abdessamad '},'11':{'r':nav.sura41, 'qori':'Zaki Daghistani'},'12':{'r':nav.sura45, 'qori':'Sahl Yassin '},'13':{'r':nav.sura49, 'qori':'Mohammed Ayyub'},'14':{'r':nav.sura53, 'qori':' Raad Al-Kurdi'},'15':{'r':nav.sura57,'qori':' Abdulrashed Soufi'}}                            
                for keys,valus in qorisura.items():             
                         if  callback_query_data.data == f'qori{keys}':
                              await bot.delete_message(callback_query_data.from_user.id, callback_query_data.message.message_id)
                              qori = valus['qori'] 
                              await bot.send_message(callback_query_data.from_user.id, f' {cd} \n <b>QORI :</b> {qori}' , reply_markup=valus['r'])
                  #keyingi ortga hm quran uchun:              
                for kenn , valu in nav.uzv.items() :
                      d=valu['t']
                      if  callback_query_data.data == f'keyingi{d}':
                              d = valu['cd']
                              dc = valu['reply']
                              await callback_query_data.message.edit_text(d, reply_markup=dc)
                          
                for knn , va in nav.uzv2.items():
                      d=va['t']
                      if  callback_query_data.data == f'ortga{d}':
                              d = va['cd']
                              dc = va['reply']
                              await callback_query_data.message.edit_text(d, reply_markup=dc)
                              
                for vare , re in jsuz.hmuchun.items():
                         if  callback_query_data.data == f'{vare}':
                             n = re['rep']
                             v = re['rep2']
                             l = re['lonk']
                             for i in range(n,v):
                             
                                 await bot.send_audio(callback_query_data.from_user.id, audio=f'{l}{i}')

                             await bot.send_message(callback_query_data.from_user.id, f'Yo\'qoridagi tugmalardan qayta foydalanishingiz mumkin ♻️ \n \n {linklar2}')
                             await bot.send_message(callback_query_data.from_user.id, text='Qorilar bo\'limiga qaytish uchun ⤵️',reply_markup=nav.orqqagaqori)
                 #############################################################
               

                if callback_query_data.data == 'keyingi':
                        await callback_query_data.message.edit_text(f'{cd3}', parse_mode='HTML',reply_markup=nav.sura2)
                          
                elif callback_query_data.data == 'keyingi2':
                                   await callback_query_data.message.edit_text(f'{cd5}', parse_mode='HTML', reply_markup=nav.sura3 )
                elif callback_query_data.data == 'keyingi3':
                                   await callback_query_data.message.edit_text(f'{cd7} ', parse_mode='HTML',reply_markup=nav.sura4 )
                
                elif callback_query_data.data == 'orqaga2':
                                   await callback_query_data.message.edit_text(f'{cd3}', parse_mode='HTML',reply_markup=nav.sura2 )
                elif callback_query_data.data == 'orqaga1':
                                   await callback_query_data.message.edit_text(f'{cd}', parse_mode='HTML',reply_markup=nav.sura1 )
                elif callback_query_data.data == 'orqaga3':
                                   await callback_query_data.message.edit_text(f'{cd5}', parse_mode='HTML',reply_markup=nav.sura3 )
                elif callback_query_data.data == 'hm1':
                        for i in range(42,56):      
                                await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/b148uz/{i}')
                        for i in range(59,74):
                                await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/b148uz/{i}')
                elif callback_query_data.data == 'hm2':
                        for i in range(73,104):
                                await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/b148uz/{i}')
                elif callback_query_data.data == 'hm3':
                        for i in range(103,134):
                                await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/b148uz/{i}')
                elif callback_query_data.data == 'hm4':
                        for i in range(133,158):
                                await bot.send_audio(callback_query_data.from_user.id, audio=f'https://t.me/b148uz/{i}')
                                
                                
               
        else:
            await bot.send_message(message.from_user.id, 'Kanallarga obuna buling 🔴⚠️ | \nkeyin /start qayta bosing ', reply_markup=nav.checksubmenu)               
@dp.message_handler()
async def botmeseg(message: types.Message):
     
    if message.chat.type == 'private':
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)) & check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID2, user_id=message.from_user.id)):
     
           if message.text == 'Quron 🎧':
              
              await bot.send_message(message.from_user.id,text=f"{qorilist}", reply_markup=nav.qorilists)
              await bot.send_message(message.from_user.id, f'  <b>Yuqoridagi tugmadan qayta foydalanishingiz mumkin ⤴️</b>', reply_markup=nav.sainmenu)
           elif message.text == 'Bot 📜':
        
               await bot.send_photo(message.from_user.id, caption=f'<b>Assalamu Alaykum ! {message.from_user.first_name}.</b> Ushbu bot @ilmziyomaskani va @elyorbekerkinbek sahifalarining rasmiy boti. Sizga foydali ma\'lumot ulashishdan hursandmiz! \n \n <a href="https://www.google.ru/maps/place/%D0%9C%D0%B0%D1%81%D0%B6%D0%B8%D0%B4+%22%D0%A2%D1%83%D1%80%D0%B0+%D0%B1%D1%83%D0%B2%D0%B0%22/@41.3495275,69.3766105,17z/data=!4m5!3m4!1s0x38aef41bf1cbe9bf:0xc38b0699d49473a5!8m2!3d41.3495985!4d69.3765563"> 📍 To\'ra Buva masjid</a> \n \n {linklar}', photo="https://t.me/b148uz/543", reply_markup=nav.sainmenu)

           elif message.text == 'Namoz ☪️':
               await bot.send_message(message.from_user.id, 'O\'zingizga kerakli bo\'limni tanlang 🔽', reply_markup=nav.namozbulimi)
           elif message.text == 'Multifilim 📺':
                   await bot.send_message(message.from_user.id, 'O\'zingizga kerakli bo\'limni tanlang 🔽', reply_markup=nav.multi)
           elif message.text == 'Qur\'onda zikri kelgan ajoyibotlar 🕋':
                for b in range(334,365):
                                await bot.send_video(message.from_user.id, video=f"https://t.me/b148uz/{b}",caption=linklar,parse_mode="HTML")
           elif message.text == 'Imom Al-buxoriy ⚜️':
                for  b in range(368,399):
                                 await bot.send_video(message.from_user.id,video=f"https://t.me/b148uz/{b}",caption=linklar,parse_mode="HTML")
                       
                                 
           elif message.text == 'Qur\'onda zikri kelgan insonlar qissasi 🏔':
                for  b in range(400,430):
                                 await bot.send_video(message.from_user.id,video=f"https://t.me/b148uz/{b}",caption=linklar,parse_mode="HTML")
           elif message.text == 'Payg\'ambarlar Tarixi ☪️':
                      await bot.send_video(message.from_user.id,video=f"https://t.me/b148uz/{400}",caption=linklar,parse_mode="HTML")
                      await bot.send_video(message.from_user.id,video=f"https://t.me/b148uz/{431}",caption=linklar,parse_mode="HTML")
           elif message.text == 'Imom Termiziy 🕯':
                for  b in range(432,438):
                                 await bot.send_video(message.from_user.id,video=f"https://t.me/b148uz/{b}",caption=linklar,parse_mode="HTML")
 
           elif message.text == 'Erkaklarga 👨‍🦰':
                
                   await bot.send_message(message.from_user.id, 'O\'zingizga kerakli bo\'limni tanlang 🔽', reply_markup=nav.namozbulimie )
           
           elif message.text == 'Ayollarga 👩‍🦰':
                    
                        
                    await bot.send_message(message.from_user.id, 'O\'zingizga kerakli bo\'limni tanlang 🔽', reply_markup=nav.namozbulimia )
                    
           elif message.text == 'Bomdod 🌃ㅤ':
                await bot.send_video(message.from_user.id, video='https://t.me/b148uz/321',caption=namoz[0], reply_markup=nav.namozbulimia, parse_mode="HTML" )
                await bot.send_video(message.from_user.id, video='https://t.me/b148uz/320',caption=namoz[1]+'\n \n'+linklar, reply_markup=nav.namozbulimia , parse_mode="HTML")
                print(namoz[3])
           elif message.text == 'Peshin 🌇ㅤ':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/324',caption=namoz[2], reply_markup=nav.namozbulimia, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/323',caption=namoz[3], reply_markup=nav.namozbulimia , parse_mode="HTML")
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/322',caption=namoz[4]+'\n \n'+linklar, reply_markup=nav.namozbulimia , parse_mode="HTML")
           elif message.text == 'Asr 🏙ㅤ':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/325',caption=namoz[5]+'\n \n'+linklar, reply_markup=nav.namozbulimia, parse_mode="HTML" )
           elif message.text == 'Shom 🌉ㅤ':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/326',caption=namoz[6], reply_markup=nav.namozbulimia, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id,video='https://t.me/b148uz/327', caption=namoz[7]+'\n \n'+linklar, reply_markup=nav.namozbulimia, parse_mode="HTML" )
           elif message.text == 'Xufton 🌌ㅤ':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/328', caption=namoz[8], reply_markup=nav.namozbulimia, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/329', caption=namoz[9], reply_markup=nav.namozbulimia, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/330',caption=namoz[10]+'\n \n'+linklar, reply_markup=nav.namozbulimia, parse_mode="HTML" )
           #////////////////////////////////////
           
           elif message.text == 'Bomdod 🌃':
                await bot.send_video(message.from_user.id, video='https://t.me/b148uz/299',caption=namoz[0], reply_markup=nav.namozbulimie, parse_mode="HTML" )
                await bot.send_video(message.from_user.id, video='https://t.me/b148uz/300',caption=namoz[1]+'\n \n'+linklar, reply_markup=nav.namozbulimie , parse_mode="HTML")
                
           elif message.text == 'Peshin 🌇':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/319',caption=namoz[2], reply_markup=nav.namozbulimie, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/305',caption=namoz[3], reply_markup=nav.namozbulimie , parse_mode="HTML")
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/318',caption=namoz[4]+'\n \n'+linklar, reply_markup=nav.namozbulimie , parse_mode="HTML")
           elif message.text == 'Asr 🏙':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/310',caption=namoz[5]+'\n \n'+linklar, reply_markup=nav.namozbulimie, parse_mode="HTML" )
           elif message.text == 'Shom 🌉':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/314',caption=namoz[6], reply_markup=nav.namozbulimie, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id,video='https://t.me/b148uz/313', caption=namoz[7]+'\n \n'+linklar, reply_markup=nav.namozbulimie, parse_mode="HTML" )
           elif message.text == 'Xufton 🌌':
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/317', caption=namoz[8], reply_markup=nav.namozbulimie, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/316', caption=namoz[9], reply_markup=nav.namozbulimie, parse_mode="HTML" )
                   await bot.send_video(message.from_user.id, video='https://t.me/b148uz/315',caption=namoz[10]+'\n \n'+linklar, reply_markup=nav.namozbulimie, parse_mode="HTML" )
           elif message.text == 'Kitobxona 🏛':
                   
                   await bot.send_message(message.from_user.id, 'O\'zingizga kerakli bo\'limni tanlang 🔽', reply_markup=nav.menukitob )  
           elif message.text == 'Kitoblar 📚':

                   await bot.send_message(message.from_user.id, f'{kutubxona.cdb} @ilmziyomaskani \n \n <b> Keyngi bo\'limga</b> ➡️', reply_markup=kutubxona.kitob1 , parse_mode="HTML")  
           elif message.text == 'Audio 🎧':
    
                   await bot.send_message(message.from_user.id, f'Audio kitoblar manba topilmadi :  @ilmziyomaskani \n \n <b> Keyngi bo\'limga</b> ➡️', parse_mode="HTML")  
                 
           elif message.text == 'Menu 📜':
                   await bot.send_message(message.from_user.id, 'O\'zingizga kerakli bo\'limni tanlang 🔽', reply_markup=nav.sainmenu )  

        else:
               await bot.send_message(message.from_user.id, 'Kanallarga obuna buling 🔴⚠️ | \nkeyin /start qayta bosing ', reply_markup=nav.checksubmenu)

@dp.callback_query_handler(text="btnqori")
async def random(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
     
            await bot.delete_message(message.from_user.id,  message.message.message_id)
            await bot.send_message(message.from_user.id , " <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML' ,reply_markup=nav.qorila)
    
    else:
            await bot.send_message(message.from_user.id, 'Kanallarga obuna buling 🔴⚠️ | \nkeyin /start qayta bosing ', reply_markup=nav.checksubmenu)
            
@dp.callback_query_handler(text="btnqori2")
async def random(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
     
            await bot.delete_message(message.from_user.id,  message.message.message_id)
            await bot.send_message(message.from_user.id , " <b>•______________________________________•ㅤ </b> \n  \n  <b>1.</b>  \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML' ,reply_markup=nav.qorila2)
    
    else:
            await bot.send_message(message.from_user.id, 'Kanallarga obuna buling 🔴⚠️ | \nkeyin /start qayta bosing ', reply_markup=nav.checksubmenu)



 
@dp.callback_query_handler(text="qoriasosiy")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)


from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.exceptions import WrongFileIdentifier
from aiogram.utils.exceptions import InvalidHTTPUrlContent
@dp.errors_handler(exception=MessageNotModified)  # for skipping this exception
async def message_not_modified_handler(update, error):
    return True

@dp.errors_handler(exception=WrongFileIdentifier)
async def Wrong_File_Identifie(update, error):
                    
                    return True
@dp.errors_handler(exception=InvalidHTTPUrlContent)
async def Invalid_HTTP_Url(update , error):
     
                    return True




if __name__ == "__main__":
    executor.start_polling(dp,loop=loop, skip_updates= True)    

      


         