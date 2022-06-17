
from os import name
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, callback_game, inline_keyboard
from aiohttp.helpers import parse_mimetype
from attr import resolve_types
' <b>.</b>  \n'
cdb = '<b>⏳ Kitob o\'qing</b> \n \n 📚 Kitoblar ro\'yxati : \n \n <b>1.</b> Saodat Asri Qisalari 1 \n <b>2.</b> Saodat Asri Qisalari 2 \n <b>3.</b> Saodat Asri Qisalari 3 \n <b>4.</b> Saodat Asri Qisalari 4 \n <b>5.</b> Oltin silsila \n <b>6.</b> Hadis va hayot 1 \n <b>7.</b> Hadis va hayot 2 \n <b>8.</b> Hadis va hayot 3 \n <b>9.</b> Hadis va hayot 4 \n <b>10.</b> Hadis va hayot 5 \n <b>11.</b> Hadis va hayot 6 \n <b>12.</b> Tafsiri hilol 1 \n <b>13.</b> Tafsiri hilol 2 \n <b>14.</b> Tafsiri hilol 3 \n <b>15.</b> Tafsiri hilol 4 \n <b>16.</b> Tafsiri hilol 5 \n <b>17.</b> Al-jome As sahih \n <b>18.</b> Quron tarjimasi \n <b>19.</b> Al-adab AL-mufrad \n <b>20.</b> Muxtasarul-viqoyi-matni \n <b>21.</b> Ibodati Islomiya \n <b>22.</b> Payg\'ambarlar tarixi \n <b>23.</b> Ichingdagi ichingdadir \n <b>24.</b> Mustahkam oila asoslari \n <b>25.</b> Men ham namoz o\'qiyman \n <b>26.</b> Mualim soniy \n <b>27.</b> Islom hazorasi \n <b>28.</b> Muxtasar islom tarixi \n <b>29.</b> islom enksiklopediyasi \n <b>30.</b> Islom ikki o\'t orasida \n \n'
cdb2 = '<b>⏳ Kitob o\'qing</b> \n \n 📚 Kitoblar ro\'yxati : \n \n <b>31.</b> Haqiqat nima \n <b>32.</b> Jannat vasfi \n <b>33.</b> Ilm olish sirlari \n <b>34.</b> Baxtli hayot sari \n <b>35.</b> Namozda xushu \n <b>36.</b> Musulmonning odobi kitobi \n <b>37.</b> Fozil odamlar shahri \n <b>38.</b> Zikr ahlidan surang \n <b>39.</b> Islom va iymon \n <b>40.</b> Aqiyda \n <b>41.</b> tajvid \n \n <b> tez orada yangi kitoblar qushiladi ♻️ </b>'
kitob1 = InlineKeyboardMarkup(row_width=6)
kitob2 = InlineKeyboardMarkup(row_width=6)
for i in range(1,200):
     
     if i < 31:
         kitob1.insert(InlineKeyboardButton(text=f'{i}',callback_data=f'kitob{i}'))
     elif i > 30 :
         if i < 42:
              kitob2.insert(InlineKeyboardButton(text=f"{i}",callback_data=f"kitob{i}"))                                          



                                     
                                     
