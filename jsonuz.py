
from attr import dataclass

#s4 teng https://t.me/shuraim1/
#s5 teng https://t.me/alquran30juzsaadalghamidi/5
#s6 teng https://t.me/bandar_abdulaziz_balilah/5 
#s7 teng https://t.me/Idriss_Akbar/388
#s8 teng https://t.me/yasseraldosari_mp3/2
#s9 teng https://t.me/juhany_mp3/5
#s10 teng https://t.me/madjmuah_1/354
#s11 teng https://t.me/Zaki_Dagistan/4
#s12 teng https://t.me/sahlyasin/4
#s13 teng https://t.me/Muhammad_Ayyub1/130
#s14 teng https://t.me/Raad_al_kurdi_mp3/123
#s15 teng https://t.me/alisufi30/3
sura = {
     '0': {'s1':'42', 's2':'257', 's3':'18', 's4':'3', 's5':'5', 's6':'5', 's7':'388', 's8':'2', 's9':'5', 's10':'354', 's11':'4', 's12':'4', 's13':'130', 's14':'123', 's15':'3'},
     '1': {'s1':'42', 's2':'257', 's3':'18', 's4':'3', 's5':'5', 's6':'5', 's7':'388', 's8':'2', 's9':'5', 's10':'354', 's11':'4', 's12':'4', 's13':'130', 's14':'123', 's15':'3'},
     '2': {'s1':'43', 's2':'258', 's3':'19', 's4':'4', 's5':'6', 's6':'6', 's7':'389', 's8':'3', 's9':'6', 's10':'355', 's11':'5', 's12':'5', 's13':'131', 's14':'124', 's15':'4'},
     '3': {'s1':'44', 's2':'259', 's3':'20', 's4':'5', 's5':'7', 's6':'7', 's7':'390', 's8':'4', 's9':'7', 's10':'356', 's11':'6', 's12':'6', 's13':'132', 's14':'125', 's15':'5'},
     '4': {'s1':'45', 's2':'260', 's3':'21', 's4':'6', 's5':'8', 's6':'8', 's7':'392', 's8':'5', 's9':'8', 's10':'357', 's11':'8', 's12':'7', 's13':'133', 's14':'126', 's15':'6'},
     '5': {'s1':'46', 's2':'261', 's3':'22', 's4':'7', 's5':'9', 's6':'9', 's7':'393', 's8':'6', 's9':'9', 's10':'358', 's11':'9', 's12':'8', 's13':'134', 's14':'127', 's15':'7'},
     '6': {'s1':'47', 's2':'262', 's3':'23', 's4':'8', 's5':'10', 's6':'10', 's7':'394', 's8':'7', 's9':'10', 's10':'359', 's11':'10', 's12':'9', 's13':'135', 's14':'128', 's15':'8'},
     '7': {'s1':'48', 's2':'263', 's3':'24', 's4':'9', 's5':'11', 's6':'11', 's7':'395', 's8':'8', 's9':'11', 's10':'360', 's11':'11', 's12':'10', 's13':'136', 's14':'129', 's15':'9'}, 
     '8': {'s1':'49', 's2':'264', 's3':'25', 's4':'10', 's5':'12', 's6':'12', 's7':'396', 's8':'9', 's9':'12', 's10':'361', 's11':'12', 's12':'11', 's13':'137', 's14':'130', 's15':'10'}, 
     '9': {'s1':'50', 's2':'265', 's3':'26', 's4':'11', 's5':'13', 's6':'13', 's7':'397', 's8':'10', 's9':'13', 's10':'362', 's11':'13', 's12':'12', 's13':'138', 's14':'131', 's15':'11'}, 
     '10': {'s1':'51', 's2':'266', 's3':'27', 's4':'12', 's5':'14', 's6':'14', 's7':'398', 's8':'11', 's9':'14', 's10':'363', 's11':'16', 's12':'13', 's13':'139', 's14':'132', 's15':'12'}, 
     '11': {'s1': '52', 's2':'267', 's3':'28', 's4':'13', 's5':'15', 's6':'15', 's7':'399', 's8':'12', 's9':'15', 's10':'364', 's11':'17', 's12':'14', 's13':'140', 's14':'133', 's15':'13'}, 
     '12': {'s1':'53', 's2':'268', 's3':'29', 's4':'14', 's5':'16', 's6':'16', 's7':'400', 's8':'13', 's9':'16', 's10':'365', 's11':'18', 's12':'15', 's13':'141', 's14':'134', 's15':'14'}, 
     '13': {'s1': '54', 's2':'269', 's3':'30', 's4':'15', 's5':'17', 's6':'17', 's7':'401', 's8':'14', 's9':'17', 's10':'366', 's11':'21', 's12':'16', 's13':'142', 's14':'135', 's15':'15'}, 
     '14': {'s1':'55', 's2':'270', 's3':'31', 's4':'16', 's5':'18', 's6':'18', 's7':'402', 's8':'15', 's9':'18', 's10':'367', 's11':'23', 's12':'17', 's13':'143', 's14':'136', 's15':'16'}, 
     '15': {'s1':'56', 's2':'271', 's3':'32', 's4':'17', 's5':'19', 's6':'19', 's7':'403', 's8':'16', 's9':'19', 's10':'368', 's11':'25', 's12':'18', 's13':'144', 's14':'137', 's15':'17'}, 
     '16': {'s1':'59', 's2':'272', 's3':'33', 's4':'18', 's5':'20', 's6':'20', 's7':'404', 's8':'17', 's9':'20', 's10':'369', 's11':'27', 's12':'19', 's13':'145', 's14':'138', 's15':'18'}, 
     '17': {'s1':'60', 's2':'273', 's3':'34', 's4':'19', 's5':'21', 's6':'21', 's7':'405', 's8':'18', 's9':'21', 's10':'370', 's11':'31', 's12':'20', 's13':'146', 's14':'139', 's15':'19'}, 
     '18' : {'s1':'61', 's2':'274', 's3':'35', 's4':'20', 's5':'22', 's6':'22', 's7':'406', 's8':'19', 's9':'22', 's10':'371', 's11':'66', 's12':'21', 's13':'147', 's14':'140', 's15':'20'}, 
     '19': {'s1':'62', 's2':'275', 's3':'36', 's4':'21', 's5':'23', 's6':'23', 's7':'407', 's8':'20', 's9':'23', 's10':'372', 's11':'67', 's12':'22', 's13':'148', 's14':'141', 's15':'21'}, 
     '20': {'s1':'63', 's2':'276', 's3':'37', 's4':'22', 's5':'24', 's6':'24', 's7':'408', 's8':'21', 's9':'24', 's10':'373', 's11':'68', 's12':'23', 's13':'149', 's14':'142', 's15':'22'}, 
     '21': {'s1':'64', 's2':'277', 's3':'38', 's4':'23', 's5':'25', 's6':'25', 's7':'409', 's8':'22', 's9':'25', 's10':'374', 's11':'69', 's12':'24', 's13':'150', 's14':'143', 's15':'23'}, 
     '22': {'s1':'65', 's2':'278', 's3':'39', 's4':'24', 's5':'26', 's6':'26', 's7':'410', 's8':'23', 's9':'26', 's10':'375', 's11':'70', 's12':'25', 's13':'151', 's14':'144', 's15':'24'}, 
     '23': {'s1':'66', 's2':'279', 's3':'40', 's4':'25', 's5':'27', 's6':'27', 's7':'411', 's8':'24', 's9':'27', 's10':'376', 's11':'71', 's12':'26', 's13':'152', 's14':'145', 's15':'25'}, 
     '24': {'s1':'67', 's2':'280', 's3':'41', 's4':'26', 's5':'28', 's6':'28', 's7':'412', 's8':'25', 's9':'28', 's10':'377', 's11':'72', 's12':'27', 's13':'153', 's14':'146', 's15':'26'}, 
     '25': {'s1':'68', 's2':'281', 's3':'42', 's4':'27', 's5':'29', 's6':'29', 's7':'413', 's8':'26', 's9':'29', 's10':'378', 's11':'73', 's12':'28', 's13':'154', 's14':'147', 's15':'27'},
     '26': {'s1':'69', 's2':'282', 's3':'43', 's4':'28', 's5':'30', 's6':'30', 's7':'414', 's8':'27', 's9':'30', 's10':'379', 's11':'74', 's12':'29', 's13':'155', 's14':'148', 's15':'28'},
     '27': {'s1':'70', 's2':'283', 's3':'44', 's4':'29', 's5':'31', 's6':'31', 's7':'415', 's8':'28', 's9':'31', 's10':'380', 's11':'75', 's12':'30', 's13':'156', 's14':'149', 's15':'29'}, 
     '28': {'s1':'71', 's2':'284', 's3':'45', 's4':'30', 's5':'32', 's6':'32', 's7':'416', 's8':'29', 's9':'32', 's10':'381', 's11':'76', 's12':'31', 's13':'157', 's14':'150', 's15':'30'}, 
     '29': {'s1':'72', 's2':'285', 's3':'46', 's4':'31', 's5':'33', 's6':'33', 's7':'417', 's8':'30', 's9':'33', 's10':'382', 's11':'77', 's12':'32', 's13':'158', 's14':'151', 's15':'31'},
     '30': {'s1':'73', 's2':'286', 's3':'47', 's4':'32', 's5':'34', 's6':'34', 's7':'418', 's8':'31', 's9':'34', 's10':'383', 's11':'78', 's12':'33', 's13':'159', 's14':'152', 's15':'32'},
     '31': {'s1':'74', 's2':'287', 's3':'48', 's4':'33', 's5':'35', 's6':'35', 's7':'419', 's8':'32', 's9':'35', 's10':'384', 's11':'79', 's12':'34', 's13':'160', 's14':'153', 's15':'33'},
     '32': {'s1':'75', 's2':'288', 's3':'49', 's4':'34', 's5':'36', 's6':'36', 's7':'420', 's8':'33', 's9':'36', 's10':'385', 's11':'80', 's12':'35', 's13':'161', 's14':'154', 's15':'34'},
     '33': {'s1':'76', 's2':'289', 's3':'50', 's4':'35', 's5':'37', 's6':'37', 's7':'421', 's8':'34', 's9':'37', 's10':'386', 's11':'81', 's12':'36', 's13':'162', 's14':'155', 's15':'35'},
     '34': {'s1':'77', 's2':'290', 's3':'51', 's4':'36', 's5':'38', 's6':'38', 's7':'422', 's8':'35', 's9':'38', 's10':'387', 's11':'82', 's12':'37', 's13':'163', 's14':'156', 's15':'36'},
     '35': {'s1':'78', 's2':'291', 's3':'52', 's4':'37', 's5':'39', 's6':'39', 's7':'423', 's8':'36', 's9':'39', 's10':'388', 's11':'83', 's12':'38', 's13':'164', 's14':'157', 's15':'37'},
     '36': {'s1':'79', 's2':'292', 's3':'53', 's4':'38', 's5':'40', 's6':'40', 's7':'424', 's8':'37', 's9':'40', 's10':'389', 's11':'84', 's12':'39', 's13':'165', 's14':'158', 's15':'38'}, 
     '37': {'s1':'80', 's2':'293', 's3':'54', 's4':'39', 's5':'41', 's6':'41', 's7':'425', 's8':'38', 's9':'41', 's10':'390', 's11':'85', 's12':'40', 's13':'166', 's14':'159', 's15':'39'},
     '38': {'s1':'81', 's2':'294', 's3':'55', 's4':'40', 's5':'42', 's6':'42', 's7':'426', 's8':'39', 's9':'42', 's10':'391', 's11':'86', 's12':'41', 's13':'167', 's14':'160', 's15':'40'},
     '39': {'s1':'82', 's2':'295', 's3':'56', 's4':'41', 's5':'43', 's6':'43', 's7':'427', 's8':'40', 's9':'43', 's10':'392', 's11':'87', 's12':'42', 's13':'168', 's14':'161', 's15':'41'},
     '40': {'s1':'83', 's2':'296', 's3':'57', 's4':'42', 's5':'44', 's6':'44', 's7':'428', 's8':'41', 's9':'44', 's10':'393', 's11':'88', 's12':'43', 's13':'169', 's14':'162', 's15':'42'},
     '41': {'s1':'84', 's2':'297', 's3':'58', 's4':'43', 's5':'45', 's6':'45', 's7':'429', 's8':'42', 's9':'45', 's10':'394', 's11':'89', 's12':'44', 's13':'170', 's14':'163', 's15':'43'},
     '42': {'s1':'85', 's2':'298', 's3':'59', 's4':'44', 's5':'46', 's6':'46', 's7':'430', 's8':'43', 's9':'46', 's10':'395', 's11':'90', 's12':'45', 's13':'171', 's14':'164', 's15':'45'},
     '43': {'s1':'86', 's2':'299', 's3':'60', 's4':'45', 's5':'47', 's6':'47', 's7':'431', 's8':'44', 's9':'47', 's10':'396', 's11':'91', 's12':'46', 's13':'172', 's14':'165', 's15':'44'},
     '44': {'s1':'87', 's2':'300', 's3':'61', 's4':'46', 's5':'48', 's6':'48', 's7':'432', 's8':'45', 's9':'48', 's10':'397', 's11':'92', 's12':'47', 's13':'173', 's14':'166', 's15':'46'},
     '45': {'s1':'88', 's2':'301', 's3':'62', 's4':'47', 's5':'49', 's6':'49', 's7':'433', 's8':'46', 's9':'49', 's10':'398', 's11':'93', 's12':'48', 's13':'174', 's14':'167', 's15':'47'},  
     '46': {'s1':'89', 's2':'302', 's3':'63', 's4':'48', 's5':'50', 's6':'50', 's7':'434', 's8':'47', 's9':'50', 's10':'399', 's11':'94', 's12':'49', 's13':'175', 's14':'168', 's15':'48'},
     '47': {'s1':'90', 's2':'303', 's3':'64', 's4':'49', 's5':'51', 's6':'51', 's7':'435', 's8':'48', 's9':'51', 's10':'400', 's11':'95', 's12':'50', 's13':'176', 's14':'169', 's15':'49'}, 
     '48': {'s1':'91', 's2':'304', 's3':'65', 's4':'50', 's5':'52', 's6':'52', 's7':'436', 's8':'49', 's9':'52', 's10':'401', 's11':'97', 's12':'51', 's13':'177', 's14':'170', 's15':'50'},
     '49': {'s1':'92', 's2':'305', 's3':'66', 's4':'51', 's5':'53', 's6':'53', 's7':'437', 's8':'50', 's9':'53', 's10':'402', 's11':'98', 's12':'52', 's13':'178', 's14':'171', 's15':'51'}, 
     '50': {'s1':'93', 's2':'306', 's3':'67', 's4':'52', 's5':'54', 's6':'54', 's7':'438', 's8':'51', 's9':'54', 's10':'403', 's11':'100', 's12':'53', 's13':'179', 's14':'172', 's15':'52'}, 
     '51': {'s1':'94', 's2':'307', 's3':'68', 's4':'53', 's5':'55', 's6':'55', 's7':'439', 's8':'52', 's9':'55', 's10':'404', 's11':'101', 's12':'54', 's13':'180', 's14':'173', 's15':'53'},
     '52': {'s1':'95', 's2':'308', 's3':'69', 's4':'54', 's5':'56', 's6':'56', 's7':'440', 's8':'53', 's9':'56', 's10':'405', 's11':'102', 's12':'55', 's13':'181', 's14':'174', 's15':'54'},
     '53': {'s1':'96', 's2':'309', 's3':'70', 's4':'55', 's5':'57', 's6':'57', 's7':'441', 's8':'54', 's9':'57', 's10':'406', 's11':'103', 's12':'56', 's13':'182', 's14':'175', 's15':'55'}, 
     '54': {'s1':'97', 's2':'310', 's3':'71', 's4':'56', 's5':'58', 's6':'58', 's7':'442', 's8':'55', 's9':'58', 's10':'407', 's11':'104', 's12':'57', 's13':'183', 's14':'176', 's15':'56'},
     '55': {'s1':'98', 's2':'311', 's3':'72', 's4':'57', 's5':'59', 's6':'59', 's7':'443', 's8':'56', 's9':'59', 's10':'408', 's11':'105', 's12':'58', 's13':'184', 's14':'177', 's15':'57'},
     '56': {'s1':'99', 's2':'312', 's3':'73', 's4':'58', 's5':'60', 's6':'60', 's7':'444', 's8':'57', 's9':'60', 's10':'409', 's11':'106', 's12':'59', 's13':'185', 's14':'178', 's15':'58'},
     '57': {'s1':'100', 's2':'313', 's3':'74', 's4':'59', 's5':'61', 's6':'61', 's7':'445', 's8':'58', 's9':'61', 's10':'410', 's11':'107', 's12':'60', 's13':'186', 's14':'179', 's15':'59'},
     '58': {'s1':'101', 's2':'314', 's3':'75', 's4':'60', 's5':'62', 's6':'62', 's7':'446', 's8':'59', 's9':'62', 's10':'411', 's11':'108', 's12':'61', 's13':'187', 's14':'180', 's15':'60'},
     '59': {'s1':'102', 's2':'315', 's3':'76', 's4':'61', 's5':'63', 's6':'63', 's7':'447', 's8':'60', 's9':'63', 's10':'412', 's11':'109', 's12':'62', 's13':'188', 's14':'181', 's15':'61'}, 
     '60': {'s1':'103', 's2':'316', 's3':'77', 's4':'62', 's5':'64', 's6':'64', 's7':'448', 's8':'61', 's9':'64', 's10':'413', 's11':'110', 's12':'63', 's13':'189', 's14':'182', 's15':'62'}, 
    #61 inlinekeyboard starts in here 

     '61': {'s1':'104', 's2':'317', 's3':'78', 's4':'63', 's5':'65', 's6':'66', 's7':'449', 's8':'62', 's9':'65', 's10':'414', 's11':'111', 's12':'64', 's13':'190', 's14':'183', 's15':'63'},
     '62': {'s1':'105', 's2':'318', 's3':'79', 's4':'64', 's5':'66', 's6':'67', 's7':'450', 's8':'63', 's9':'66', 's10':'415', 's11':'112', 's12':'65', 's13':'191', 's14':'184', 's15':'64'}, 
     '63': {'s1':'106', 's2':'319', 's3':'80', 's4':'65', 's5':'67', 's6':'68', 's7':'451', 's8':'64', 's9':'67', 's10':'416', 's11':'113', 's12':'66', 's13':'192', 's14':'185', 's15':'65'},
     '64': {'s1':'107', 's2':'320', 's3':'81', 's4':'66', 's5':'68', 's6':'69', 's7':'452', 's8':'65', 's9':'68', 's10':'417', 's11':'114', 's12':'67', 's13':'193', 's14':'186', 's15':'66'},
     '65': {'s1':'108', 's2':'321', 's3':'82', 's4':'67', 's5':'69', 's6':'70', 's7':'453', 's8':'66', 's9':'69', 's10':'418', 's11':'115', 's12':'68', 's13':'194', 's14':'187', 's15':'67'},
     '66': {'s1':'109', 's2':'322', 's3':'83', 's4':'68', 's5':'70', 's6':'71', 's7':'454', 's8':'67', 's9':'70', 's10':'419', 's11':'116', 's12':'69', 's13':'195', 's14':'188', 's15':'68'}, 
     '67': {'s1':'110', 's2':'323', 's3':'84', 's4':'69', 's5':'71', 's6':'72', 's7':'455', 's8':'68', 's9':'71', 's10':'420', 's11':'117', 's12':'70', 's13':'196', 's14':'189', 's15':'69'},
     '68': {'s1':'111', 's2':'324', 's3':'85', 's4':'117', 's5':'72', 's6':'73', 's7':'456', 's8':'69', 's9':'72', 's10':'421', 's11':'118', 's12':'71', 's13':'197', 's14':'190', 's15':'70'},
     '69': {'s1':'112', 's2':'325', 's3':'86', 's4':'118', 's5':'73', 's6':'74', 's7':'457', 's8':'70', 's9':'73', 's10':'422', 's11':'119', 's12':'72', 's13':'198', 's14':'191', 's15':'71'}, 
     '70': {'s1':'113', 's2':'326', 's3':'87', 's4':'119', 's5':'74', 's6':'75', 's7':'458', 's8':'71', 's9':'74', 's10':'423', 's11':'120', 's12':'73', 's13':'199', 's14':'192', 's15':'72'}, 
     '71': {'s1':'114', 's2':'327', 's3':'88', 's4':'120', 's5':'75', 's6':'76', 's7':'459', 's8':'72', 's9':'75', 's10':'424', 's11':'121', 's12':'74', 's13':'200', 's14':'193', 's15':'73'}, 
     '72': {'s1':'115', 's2':'328', 's3':'89', 's4':'121', 's5':'76', 's6':'77', 's7':'460', 's8':'73', 's9':'76', 's10':'425', 's11':'122', 's12':'75', 's13':'201', 's14':'194', 's15':'74'}, 
     '73': {'s1':'116', 's2':'329', 's3':'90', 's4':'122', 's5':'77', 's6':'78', 's7':'461', 's8':'74', 's9':'77', 's10':'426', 's11':'123', 's12':'76', 's13':'203', 's14':'195', 's15':'75'}, 
     '74': {'s1':'117', 's2':'330', 's3':'91', 's4':'123', 's5':'78', 's6':'79', 's7':'462', 's8':'75', 's9':'78', 's10':'427', 's11':'124', 's12':'77', 's13':'204', 's14':'196', 's15':'76'}, 
     '75': {'s1':'118', 's2':'331', 's3':'92', 's4':'124', 's5':'79', 's6':'80', 's7':'463', 's8':'76', 's9':'79', 's10':'428', 's11':'125', 's12':'78', 's13':'205', 's14':'197', 's15':'77'}, 
     '76': {'s1':'119', 's2':'332', 's3':'93', 's4':'125', 's5':'80', 's6':'81', 's7':'464', 's8':'77', 's9':'80', 's10':'429', 's11':'126', 's12':'79', 's13':'206', 's14':'198', 's15':'78'}, 
     '77': {'s1':'120', 's2':'333', 's3':'94', 's4':'126', 's5':'81', 's6':'82', 's7':'465', 's8':'78', 's9':'81', 's10':'430', 's11':'127', 's12':'80', 's13':'207', 's14':'199', 's15':'79'}, 
     '78': {'s1':'121', 's2':'334', 's3':'95', 's4':'127', 's5':'82', 's6':'83', 's7':'466', 's8':'79', 's9':'82', 's10':'431', 's11':'128', 's12':'81', 's13':'208', 's14':'200', 's15':'80'}, 
     '79': {'s1':'122', 's2':'335', 's3':'96', 's4':'128', 's5':'83', 's6':'84', 's7':'467', 's8':'80', 's9':'83', 's10':'432', 's11':'129', 's12':'82', 's13':'209', 's14':'201', 's15':'81'}, 
     '80': {'s1':'123', 's2':'336', 's3':'97', 's4':'129', 's5':'84', 's6':'85', 's7':'468', 's8':'81', 's9':'84', 's10':'433', 's11':'130', 's12':'83', 's13':'210', 's14':'202', 's15':'82'}, 
     '81': {'s1':'124', 's2':'337', 's3':'98', 's4':'130', 's5':'85', 's6':'86', 's7':'469', 's8':'82', 's9':'85', 's10':'434', 's11':'131', 's12':'84', 's13':'211', 's14':'203', 's15':'83'}, 
     '82': {'s1':'125', 's2':'338', 's3':'99', 's4':'131', 's5':'86', 's6':'87', 's7':'470', 's8':'83', 's9':'86', 's10':'435', 's11':'132', 's12':'85', 's13':'212', 's14':'204', 's15':'84'}, 
     '83': {'s1':'126', 's2':'339', 's3':'100', 's4':'132', 's5':'87', 's6':'88', 's7':'471', 's8':'84', 's9':'87', 's10':'436', 's11':'141', 's12':'86', 's13':'213', 's14':'205', 's15':'85'},
     '84': {'s1':'127', 's2':'340', 's3':'101', 's4':'133', 's5':'88', 's6':'89', 's7':'472', 's8':'85', 's9':'88', 's10':'437', 's11':'142', 's12':'87', 's13':'214', 's14':'206', 's15':'86'}, 
     '85': {'s1':'128', 's2':'341', 's3':'102', 's4':'134', 's5':'89', 's6':'90', 's7':'473', 's8':'86', 's9':'89', 's10':'438', 's11':'143', 's12':'88', 's13':'215', 's14':'207', 's15':'87'}, 
     '86': {'s1':'129', 's2':'342', 's3':'103', 's4':'135', 's5':'90', 's6':'91', 's7':'474', 's8':'87', 's9':'90', 's10':'439', 's11':'144', 's12':'89', 's13':'216', 's14':'208', 's15':'88'},
     '87': {'s1':'130', 's2':'343', 's3':'104', 's4':'136', 's5':'91', 's6':'92', 's7':'475', 's8':'88', 's9':'91', 's10':'440', 's11':'145', 's12':'90', 's13':'217', 's14':'209', 's15':'89'}, 
     '88': {'s1':'131', 's2':'344', 's3':'105', 's4':'137', 's5':'92', 's6':'93', 's7':'476', 's8':'89', 's9':'92', 's10':'441', 's11':'146', 's12':'91', 's13':'218', 's14':'210', 's15':'90'}, 
     '89': {'s1':'132', 's2':'345', 's3':'106', 's4':'138', 's5':'93', 's6':'94', 's7':'477', 's8':'90', 's9':'93', 's10':'442', 's11':'147', 's12':'92', 's13':'219', 's14':'211', 's15':'91'}, 
     '90': {'s1':'133', 's2':'346', 's3':'107', 's4':'139', 's5':'94', 's6':'95', 's7':'478', 's8':'91', 's9':'94', 's10':'443', 's11':'148', 's12':'93', 's13':'220', 's14':'212', 's15':'92'}, 
     '91': {'s1':'134', 's2':'347', 's3':'108', 's4':'140', 's5':'95', 's6':'96', 's7':'479', 's8':'92', 's9':'95', 's10':'444', 's11':'149', 's12':'94', 's13':'221', 's14':'213', 's15':'93'}, 
     '92': {'s1':'135', 's2':'348', 's3':'109', 's4':'141', 's5':'96', 's6':'97', 's7':'480', 's8':'93', 's9':'96', 's10':'445', 's11':'150', 's12':'95', 's13':'222', 's14':'214', 's15':'94'}, 
     '93': {'s1':'136', 's2':'349', 's3':'110', 's4':'142', 's5':'97', 's6':'98', 's7':'481', 's8':'94', 's9':'97', 's10':'446', 's11':'151', 's12':'96', 's13':'223', 's14':'215', 's15':'95'}, 
     '94': {'s1':'137', 's2':'350', 's3':'111', 's4':'143', 's5':'98', 's6':'99', 's7':'482', 's8':'95', 's9':'98', 's10':'447', 's11':'152', 's12':'97', 's13':'224', 's14':'216', 's15':'96'}, 
     '95': {'s1':'138', 's2':'351', 's3':'112', 's4':'144', 's5':'99', 's6':'100', 's7':'483', 's8':'96', 's9':'99', 's10':'448', 's11':'153', 's12':'98', 's13':'225', 's14':'217', 's15':'97'}, 
     '96': {'s1':'139', 's2':'352', 's3':'113', 's4':'145', 's5':'100', 's6':'101', 's7':'484', 's8':'97', 's9':'100', 's10':'449', 's11':'158', 's12':'99', 's13':'226', 's14':'218', 's15':'98'}, 
     '97': {'s1':'140', 's2':'353', 's3':'114', 's4':'146', 's5':'101', 's6':'102', 's7':'485', 's8':'98', 's9':'101', 's10':'450', 's11':'159', 's12':'100', 's13':'227', 's14':'219', 's15':'99'}, 
     '98': {'s1':'141', 's2':'354', 's3':'115', 's4':'147', 's5':'102', 's6':'103', 's7':'486', 's8':'99', 's9':'102', 's10':'451', 's11':'160', 's12':'101', 's13':'228', 's14':'220', 's15':'100'},
     '99': {'s1':'142', 's2':'355', 's3':'116', 's4':'148', 's5':'103', 's6':'104', 's7':'487', 's8':'100', 's9':'103', 's10':'452', 's11':'161', 's12':'102', 's13':'229', 's14':'221', 's15':'101'}, 
     '100': {'s1':'143', 's2':'356', 's3':'117', 's4':'149', 's5':'104', 's6':'105', 's7':'488', 's8':'101', 's9':'104', 's10':'453', 's11':'162', 's12':'103', 's13':'230', 's14':'222', 's15':'102'}, 
     '101': {'s1':'144', 's2':'357', 's3':'118', 's4':'150', 's5':'105', 's6':'106', 's7':'489', 's8':'102', 's9':'105', 's10':'454', 's11':'169', 's12':'104', 's13':'231', 's14':'223', 's15':'114'}, 
     '102': {'s1':'145', 's2':'358', 's3':'119', 's4':'151', 's5':'106', 's6':'107', 's7':'490', 's8':'103', 's9':'106', 's10':'455', 's11':'170', 's12':'105', 's13':'232', 's14':'224', 's15':'103'}, 
     '103': {'s1':'146', 's2':'359', 's3':'120', 's4':'152', 's5':'107', 's6':'108', 's7':'491', 's8':'104', 's9':'107', 's10':'456', 's11':'171', 's12':'106', 's13':'233', 's14':'225', 's15':'104'}, 
     '104': {'s1':'147', 's2':'360', 's3':'121', 's4':'153', 's5':'108', 's6':'109', 's7':'492', 's8':'105', 's9':'108', 's10':'457', 's11':'172', 's12':'107', 's13':'234', 's14':'226', 's15':'105'}, 
     '105': {'s1':'148', 's2':'361', 's3':'122', 's4':'154', 's5':'109', 's6':'110', 's7':'493', 's8':'106', 's9':'109', 's10':'458', 's11':'173', 's12':'108', 's13':'235', 's14':'227', 's15':'106'}, 
     '106': {'s1':'149', 's2':'362', 's3':'123', 's4':'155', 's5':'110', 's6':'111', 's7':'494', 's8':'107', 's9':'110', 's10':'459', 's11':'174', 's12':'109', 's13':'236', 's14':'228', 's15':'107'}, 
     '107': {'s1':'150', 's2':'363', 's3':'124', 's4':'156', 's5':'111', 's6':'112', 's7':'495', 's8':'108', 's9':'111', 's10':'460', 's11':'175', 's12':'100', 's13':'237', 's14':'229', 's15':'108'}, 
     '108': {'s1':'151', 's2':'364', 's3':'125', 's4':'157', 's5':'112', 's6':'113', 's7':'496', 's8':'109', 's9':'112', 's10':'461', 's11':'176', 's12':'111', 's13':'238', 's14':'230', 's15':'109'}, 
     '109': {'s1':'152', 's2':'365', 's3':'126', 's4':'158', 's5':'113', 's6':'114', 's7':'497', 's8':'110', 's9':'113', 's10':'462', 's11':'177', 's12':'112', 's13':'239', 's14':'231', 's15':'110'}, 
     '110': {'s1':'153', 's2':'366', 's3':'127', 's4':'159', 's5':'114', 's6':'115', 's7':'498', 's8':'111', 's9':'114', 's10':'463', 's11':'178', 's12':'113', 's13':'240', 's14':'232', 's15':'111'}, 
     '111': {'s1':'154', 's2':'367', 's3':'128', 's4':'160', 's5':'115', 's6':'116', 's7':'499', 's8':'112', 's9':'115', 's10':'464', 's11':'179', 's12':'114', 's13':'241', 's14':'233', 's15':'112'}, 
     '112': {'s1':'155', 's2':'368', 's3':'129', 's4':'161', 's5':'116', 's6':'117', 's7':'500', 's8':'113', 's9':'116', 's10':'465', 's11':'180', 's12':'115', 's13':'242', 's14':'234', 's15':'113'}, 
     '113': {'s1':'156', 's2':'369', 's3':'130', 's4':'162', 's5':'117', 's6':'118', 's7':'501', 's8':'114', 's9':'117', 's10':'466', 's11':'181', 's12':'116', 's13':'243', 's14':'235', 's15':'115'}, 
     '114': {'s1':'157', 's2':'370', 's3':'131', 's4':'163', 's5':'118', 's6':'119', 's7':'502', 's8':'115', 's9':'118', 's10':'467', 's11':'182', 's12':'117', 's13':'244', 's14':'236', 's15':'116'},
     
     
      }

# bbc = {'22':'11', 'n':{
#     '55':'56',
#     '55':'58',
#     '55':'59',
#     '55':'555',


# }}

kitoblink = {
       '1':{'b1':'487'},'2':{'b1':'488'},'3':{'b1':'489'},'4':{'b1':'490'},'5':{'b1':'527'},
      '6':{'b1':'491'},'7':{'b1':'492'},'8':{'b1':'493'},'9':{'b1':'494'},'10':{'b1':'495'},
    '11': {'b1':'496'},'12': {'b1':'528'}, '13': {'b1':'529'}, '14': {'b1':'530'}, '15': {'b1':'531'}, '16': {'b1':'532'}, '17': {'b1':'533'}, 
    '18': {'b1':'534'}, '19': {'b1':'535'}, '20': {'b1':'536'}, '21': {'b1':'503'}, '22': {'b1':'504'}, '23': {'b1':'505'}, '24': {'b1':'506'}, 
    '25': {'b1':'507'}, '26': {'b1':'508'}, '27': {'b1':'509'}, '28': {'b1':'510'}, '29': {'b1':'512'}, '30': {'b1':'513'}, '31': {'b1':'514'}, 
    '32': {'b1':'515'}, '33': {'b1':'516'}, '34': {'b1':'517'}, '35': {'b1':'519'}, '36': {'b1':'520'}, '37': {'b1':'522'}, '38': {'b1':'523'}, 
    '39' : {'b1':'524'}, '40':{'b1':'526'},'41':{'b1':'525'}
      
}


hmuchun = {
      'hm5':{
            'rep':257,
            'rep2':286,
            'lonk':'https://t.me/MisharyRoshidQuran/',
            
      },
      'hm6':{
            'rep':288,
            'rep2':317,
            'lonk':'https://t.me/MisharyRoshidQuran/',
      },
      'hm7':{
            'rep':317,
            'rep2':347,
            'lonk':'https://t.me/MisharyRoshidQuran/',
      },
      'hm8':{
            'rep':347,
            'rep2':371,
            'lonk':'https://t.me/MisharyRoshidQuran/',
      },
      'hm9':{
            'rep':18,
            'rep2':48,
            'lonk':'https://t.me/Sheikh_Abdul_Rahman_Al_Sudais/',
            
      },
      'hm10':{
            'rep':48,
            'rep2':78,
            'lonk':'https://t.me/Sheikh_Abdul_Rahman_Al_Sudais/',
      },
      'hm11':{
            'rep':78,
            'rep2':108,
            'lonk':'https://t.me/Sheikh_Abdul_Rahman_Al_Sudais/',
      },
      'hm12':{
            'rep':108,
            'rep2':137,
            'lonk':'https://t.me/Sheikh_Abdul_Rahman_Al_Sudais/',
      },
      #s4 ga teng
      'hm13':{
            'rep':3,
            'rep2':33,
            'lonk':'https://t.me/shuraim1/',
      },
      'hm14':{
            'rep':31,
            'rep2':61,
            'lonk':'https://t.me/shuraim1/',
      },
      'hm15':{
            'rep':61,
            'rep2':91,
            'lonk':'https://t.me/shuraim1/',
      },
      'hm16':{
            'rep':139,
            'rep2':164,
            'lonk':'https://t.me/shuraim1/',
      },
      #s5 ga teng
       'hm17':{
            'rep':5,
            'rep2':35,
            'lonk':'https://t.me/alquran30juzsaadalghamidi/',
      },
      'hm18':{
            'rep':35,
            'rep2':65,
            'lonk':'https://t.me/alquran30juzsaadalghamidi/',
      },
      'hm19':{
            'rep':65,
            'rep2':95,
            'lonk':'https://t.me/alquran30juzsaadalghamidi/',
      },
      'hm20':{
            'rep':95,
            'rep2':119,
            'lonk':'https://t.me/alquran30juzsaadalghamidi/',
      },
      #s6 ga teng
      'hm21':{
            'rep':5,
            'rep2':35,
            'lonk':'https://t.me/bandar_abdulaziz_balilah/'
      },
      'hm22':{
            'rep':35,
            'rep2':65,
            'lonk':'https://t.me/bandar_abdulaziz_balilah/'
      },
      'hm23':{
            'rep':66,
            'rep2':96,
            'lonk':'https://t.me/bandar_abdulaziz_balilah/'
      },
      'hm24':{
            'rep':96,
            'rep2':120,
            'lonk':'https://t.me/bandar_abdulaziz_balilah/'
      },
      #s7 ga teng 
       'hm25':{
            'rep':392,
            'rep2':419,
            'lonk':'https://t.me/Idriss_Akbar/'
      },
      'hm26':{
            'rep':419,
            'rep2':449,
            'lonk':'https://t.me/Idriss_Akbar/'
      },
      'hm27':{
            'rep':449,
            'rep2':479,
            'lonk':'https://t.me/Idriss_Akbar/'
      },
      'hm28':{
            'rep':479,
            'rep2':503,
            'lonk':'https://t.me/Idriss_Akbar/'
      },
      #s8 ga teng
       'hm29':{
            'rep':2,
            'rep2':32,
            'lonk':'https://t.me/yasseraldosari_mp3/'
      },
      'hm30':{
            'rep':32,
            'rep2':62,
            'lonk':'https://t.me/yasseraldosari_mp3/'
      },
      'hm31':{
            'rep':62,
            'rep2':92,
            'lonk':'https://t.me/yasseraldosari_mp3/'
      },
      'hm32':{
            'rep':91,
            'rep2':116,
            'lonk':'https://t.me/yasseraldosari_mp3/'
      },
      #s9 ga teng
       'hm33':{
            'rep':5,
            'rep2':35,
            'lonk':'https://t.me/juhany_mp3/'
      },
      'hm34':{
            'rep':35,
            'rep2':65,
            'lonk':'https://t.me/juhany_mp3/'
      },
      'hm35':{
            'rep':65,
            'rep2':96,
            'lonk':'https://t.me/juhany_mp3/'
      },
      'hm36':{
            'rep':96,
            'rep2':119,
            'lonk':'https://t.me/juhany_mp3/'
      },
       #s10 ga teng
       'hm37':{
            'rep':354,
            'rep2':384,
            'lonk':'https://t.me/madjmuah_1/'
      },
      'hm38':{
            'rep':384,
            'rep2':414,
            'lonk':'https://t.me/madjmuah_1/'
      },
      'hm39':{
            'rep':414,
            'rep2':444,
            'lonk':'https://t.me/madjmuah_1/'
      },
      'hm40':{
            'rep':443,
            'rep2':468,
            'lonk':'https://t.me/madjmuah_1/'
      },
       #s11 ga teng
       'hm41':{
            'rep':66,
            'rep2':95,
            'lonk':'https://t.me/madjmuah_1/'
      },
      'hm42':{
            'rep':111,
            'rep2':132,
            'lonk':'https://t.me/madjmuah_1/'
      },
      'hm43':{
            'rep':141,
            'rep2':160,
            'lonk':'https://t.me/madjmuah_1/'
      },
      'hm44':{
            'rep':160,
            'rep2':182,
            'lonk':'https://t.me/madjmuah_1/'
      },
       #s12 ga teng
       'hm45':{
            'rep':4,
            'rep2':34,
            'lonk':'https://t.me/sahlyasin/'
      },
      'hm46':{
            'rep':34,
            'rep2':64,
            'lonk':'https://t.me/sahlyasin/'
      },
      'hm47':{
            'rep':64,
            'rep2':94,
            'lonk':'https://t.me/sahlyasin/'
      },
      'hm48':{
            'rep':94,
            'rep2':118,
            'lonk':'https://t.me/sahlyasin/'
      },
              #s13 ga teng
       'hm49':{
            'rep':130,
            'rep2':160,
            'lonk':'https://t.me/Muhammad_Ayyub1/'
      },
      'hm50':{
            'rep':160,
            'rep2':190,
            'lonk':'https://t.me/Muhammad_Ayyub1/'
      },
      'hm51':{
            'rep':190,
            'rep2':220,
            'lonk':'https://t.me/Muhammad_Ayyub1/'
      },
      'hm52':{
            'rep':219,
            'rep2':245,
            'lonk':'https://t.me/Muhammad_Ayyub1/'
      },
         #s14 ga teng
       'hm53':{
            'rep':123,
            'rep2':153,
            'lonk':'https://t.me/Raad_al_kurdi_mp3/'
      },
      'hm54':{
            'rep':152,
            'rep2':183,
            'lonk':'https://t.me/Raad_al_kurdi_mp3/'
      },
      'hm55':{
            'rep':183,
            'rep2':213,
            'lonk':'https://t.me/Raad_al_kurdi_mp3/'
      },
      'hm56':{
            'rep':213,
            'rep2':237,
            'lonk':'https://t.me/Raad_al_kurdi_mp3/'
      },   
       #s15 ga teng
       'hm57':{
            'rep':3,
            'rep2':33,
            'lonk':'https://t.me/alisufi30/'
      },
      'hm58':{
            'rep':33,
            'rep2':63,
            'lonk':'https://t.me/alisufi30/'
      },
      'hm59':{
            'rep':62,
            'rep2':93,
            'lonk':'https://t.me/alisufi30/'
      },
      'hm60':{
            'rep':92,
            'rep2':117,
            'lonk':'https://t.me/alisufi30/'
      },   
}
