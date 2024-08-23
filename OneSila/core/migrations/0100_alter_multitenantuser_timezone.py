# Generated by Django 5.0.2 on 2024-06-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0099_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('America/Matamoros', 'America/Matamoros'), ('America/Santarem', 'America/Santarem'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Europe/Andorra', 'Europe/Andorra'), ('Europe/Budapest', 'Europe/Budapest'), ('Australia/NSW', 'Australia/NSW'), ('America/St_Johns', 'America/St_Johns'), ('America/Regina', 'America/Regina'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Dominica', 'America/Dominica'), ('America/Recife', 'America/Recife'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Chicago', 'America/Chicago'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Europe/Vatican', 'Europe/Vatican'), ('Europe/Belgrade', 'Europe/Belgrade'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/Chihuahua', 'America/Chihuahua'), ('US/Mountain', 'US/Mountain'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Asia/Chungking', 'Asia/Chungking'), ('Asia/Chita', 'Asia/Chita'), ('Asia/Karachi', 'Asia/Karachi'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Europe/Saratov', 'Europe/Saratov'), ('Pacific/Apia', 'Pacific/Apia'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Australia/Perth', 'Australia/Perth'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Asia/Manila', 'Asia/Manila'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Indian/Maldives', 'Indian/Maldives'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Nipigon', 'America/Nipigon'), ('MST7MDT', 'MST7MDT'), ('America/Virgin', 'America/Virgin'), ('Europe/Vienna', 'Europe/Vienna'), ('ROK', 'ROK'), ('US/Samoa', 'US/Samoa'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Africa/Douala', 'Africa/Douala'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Jamaica', 'Jamaica'), ('Cuba', 'Cuba'), ('Asia/Katmandu', 'Asia/Katmandu'), ('EET', 'EET'), ('America/Ojinaga', 'America/Ojinaga'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Africa/Malabo', 'Africa/Malabo'), ('Brazil/Acre', 'Brazil/Acre'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Hongkong', 'Hongkong'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/Toronto', 'America/Toronto'), ('America/Lima', 'America/Lima'), ('Africa/Harare', 'Africa/Harare'), ('America/Fortaleza', 'America/Fortaleza'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Montevideo', 'America/Montevideo'), ('Africa/Nairobi', 'Africa/Nairobi'), ('US/East-Indiana', 'US/East-Indiana'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Madrid', 'Europe/Madrid'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Resolute', 'America/Resolute'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Africa/Lagos', 'Africa/Lagos'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Louisville', 'America/Louisville'), ('Australia/Victoria', 'Australia/Victoria'), ('Africa/Tunis', 'Africa/Tunis'), ('Egypt', 'Egypt'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Europe/Skopje', 'Europe/Skopje'), ('Asia/Macau', 'Asia/Macau'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('CST6CDT', 'CST6CDT'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Brussels', 'Europe/Brussels'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Australia/ACT', 'Australia/ACT'), ('America/Bahia', 'America/Bahia'), ('Canada/Central', 'Canada/Central'), ('America/Santiago', 'America/Santiago'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Europe/Paris', 'Europe/Paris'), ('Navajo', 'Navajo'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Africa/Accra', 'Africa/Accra'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Moncton', 'America/Moncton'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Africa/Algiers', 'Africa/Algiers'), ('NZ', 'NZ'), ('Poland', 'Poland'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Noronha', 'America/Noronha'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Asia/Dacca', 'Asia/Dacca'), ('Europe/Malta', 'Europe/Malta'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('HST', 'HST'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Barbados', 'America/Barbados'), ('Australia/Eucla', 'Australia/Eucla'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Atlantic/Azores', 'Atlantic/Azores'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('America/Swift_Current', 'America/Swift_Current'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Montserrat', 'America/Montserrat'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Nuuk', 'America/Nuuk'), ('Brazil/West', 'Brazil/West'), ('Libya', 'Libya'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Etc/UTC', 'Etc/UTC'), ('America/Juneau', 'America/Juneau'), ('Europe/Busingen', 'Europe/Busingen'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Etc/GMT0', 'Etc/GMT0'), ('Africa/Maputo', 'Africa/Maputo'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Amman', 'Asia/Amman'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('America/Menominee', 'America/Menominee'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Halifax', 'America/Halifax'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Etc/GMT-2', 'Etc/GMT-2'), ('W-SU', 'W-SU'), ('Turkey', 'Turkey'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Thule', 'America/Thule'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Dawson', 'America/Dawson'), ('America/Havana', 'America/Havana'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('America/St_Thomas', 'America/St_Thomas'), ('Asia/Dili', 'Asia/Dili'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Greenwich', 'Greenwich'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Zulu', 'Zulu'), ('America/La_Paz', 'America/La_Paz'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Asia/Oral', 'Asia/Oral'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('CET', 'CET'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Detroit', 'America/Detroit'), ('America/Adak', 'America/Adak'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Asia/Damascus', 'Asia/Damascus'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Edmonton', 'America/Edmonton'), ('America/Curacao', 'America/Curacao'), ('Asia/Tokyo', 'Asia/Tokyo'), ('build/etc/localtime', 'build/etc/localtime'), ('America/New_York', 'America/New_York'), ('Iceland', 'Iceland'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Europe/Berlin', 'Europe/Berlin'), ('Europe/Guernsey', 'Europe/Guernsey'), ('America/Cayman', 'America/Cayman'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Taipei', 'Asia/Taipei'), ('Africa/Cairo', 'Africa/Cairo'), ('America/Jamaica', 'America/Jamaica'), ('US/Central', 'US/Central'), ('America/Monterrey', 'America/Monterrey'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Guatemala', 'America/Guatemala'), ('Asia/Kuching', 'Asia/Kuching'), ('Asia/Qatar', 'Asia/Qatar'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Africa/Asmera', 'Africa/Asmera'), ('UCT', 'UCT'), ('Europe/Jersey', 'Europe/Jersey'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('EST5EDT', 'EST5EDT'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Cuiaba', 'America/Cuiaba'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('GB-Eire', 'GB-Eire'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Pacific/Easter', 'Pacific/Easter'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Maceio', 'America/Maceio'), ('America/Shiprock', 'America/Shiprock'), ('America/Goose_Bay', 'America/Goose_Bay'), ('US/Eastern', 'US/Eastern'), ('America/Boise', 'America/Boise'), ('WET', 'WET'), ('Asia/Tehran', 'Asia/Tehran'), ('Africa/Juba', 'Africa/Juba'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Africa/Freetown', 'Africa/Freetown'), ('Europe/Podgorica', 'Europe/Podgorica'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Hermosillo', 'America/Hermosillo'), ('Africa/Niamey', 'Africa/Niamey'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Denver', 'America/Denver'), ('Iran', 'Iran'), ('America/Anchorage', 'America/Anchorage'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Africa/Banjul', 'Africa/Banjul'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('GMT', 'GMT'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/Rosario', 'America/Rosario'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Australia/Brisbane', 'Australia/Brisbane'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Paramaribo', 'America/Paramaribo'), ('Etc/Zulu', 'Etc/Zulu'), ('Australia/LHI', 'Australia/LHI'), ('America/Montreal', 'America/Montreal'), ('America/Guyana', 'America/Guyana'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Dubai', 'Asia/Dubai'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Africa/Kigali', 'Africa/Kigali'), ('Pacific/Bougainville', 'Pacific/Bougainville'),
                                   ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Indianapolis', 'America/Indianapolis'), ('Pacific/Niue', 'Pacific/Niue'), ('Europe/Sofia', 'Europe/Sofia'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Europe/Belfast', 'Europe/Belfast'), ('Mexico/General', 'Mexico/General'), ('Asia/Colombo', 'Asia/Colombo'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Indian/Reunion', 'Indian/Reunion'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Chile/Continental', 'Chile/Continental'), ('Universal', 'Universal'), ('America/Managua', 'America/Managua'), ('America/Miquelon', 'America/Miquelon'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/Asuncion', 'America/Asuncion'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Antigua', 'America/Antigua'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Asia/Aden', 'Asia/Aden'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Indian/Chagos', 'Indian/Chagos'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Pacific/Yap', 'Pacific/Yap'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Europe/Helsinki', 'Europe/Helsinki'), ('GMT-0', 'GMT-0'), ('Japan', 'Japan'), ('Asia/Harbin', 'Asia/Harbin'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Mendoza', 'America/Mendoza'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Factory', 'Factory'), ('Asia/Muscat', 'Asia/Muscat'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Manaus', 'America/Manaus'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('UTC', 'UTC'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Australia/North', 'Australia/North'), ('US/Pacific', 'US/Pacific'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Atka', 'America/Atka'), ('America/El_Salvador', 'America/El_Salvador'), ('Etc/GMT-6', 'Etc/GMT-6'), ('ROC', 'ROC'), ('America/Guadeloupe', 'America/Guadeloupe'), ('GMT0', 'GMT0'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Eire', 'Eire'), ('Portugal', 'Portugal'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Etc/GMT+4', 'Etc/GMT+4'), ('America/Caracas', 'America/Caracas'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Nassau', 'America/Nassau'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Belize', 'America/Belize'), ('PRC', 'PRC'), ('America/Belem', 'America/Belem'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Asia/Singapore', 'Asia/Singapore'), ('Etc/GMT', 'Etc/GMT'), ('Europe/Samara', 'Europe/Samara'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Pacific/Truk', 'Pacific/Truk'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Asia/Brunei', 'Asia/Brunei'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Europe/Tirane', 'Europe/Tirane'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('America/Iqaluit', 'America/Iqaluit'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Macao', 'Asia/Macao'), ('Africa/Conakry', 'Africa/Conakry'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Guayaquil', 'America/Guayaquil'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('US/Michigan', 'US/Michigan'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Europe/Rome', 'Europe/Rome'), ('America/Eirunepe', 'America/Eirunepe'), ('Indian/Christmas', 'Indian/Christmas'), ('America/St_Lucia', 'America/St_Lucia'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Australia/Adelaide', 'Australia/Adelaide'), ('America/Phoenix', 'America/Phoenix'), ('Asia/Hebron', 'Asia/Hebron'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Europe/London', 'Europe/London'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Asia/Magadan', 'Asia/Magadan'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Godthab', 'America/Godthab'), ('America/Martinique', 'America/Martinique'), ('MST', 'MST'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Mexico_City', 'America/Mexico_City'), ('America/Bogota', 'America/Bogota'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Australia/Hobart', 'Australia/Hobart'), ('America/Atikokan', 'America/Atikokan'), ('Brazil/East', 'Brazil/East'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Israel', 'Israel'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('GB', 'GB'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Rainy_River', 'America/Rainy_River'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Prague', 'Europe/Prague'), ('Australia/South', 'Australia/South'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Metlakatla', 'America/Metlakatla'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('America/Nome', 'America/Nome'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Whitehorse', 'America/Whitehorse'), ('US/Alaska', 'US/Alaska'), ('America/Panama', 'America/Panama'), ('Indian/Comoro', 'Indian/Comoro'), ('Asia/Seoul', 'Asia/Seoul'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Singapore', 'Singapore'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Ensenada', 'America/Ensenada'), ('America/Anguilla', 'America/Anguilla'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Africa/Bamako', 'Africa/Bamako'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Creston', 'America/Creston'), ('America/Inuvik', 'America/Inuvik'), ('America/Merida', 'America/Merida'), ('MET', 'MET'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Indian/Cocos', 'Indian/Cocos'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Pacific/Midway', 'Pacific/Midway'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Indian/Mauritius', 'Indian/Mauritius'), ('US/Hawaii', 'US/Hawaii'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Europe/Volgograd', 'Europe/Volgograd'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Asia/Makassar', 'Asia/Makassar'), ('Africa/Lome', 'Africa/Lome'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Vancouver', 'America/Vancouver'), ('America/Aruba', 'America/Aruba'), ('America/St_Kitts', 'America/St_Kitts'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Europe/Minsk', 'Europe/Minsk'), ('Asia/Yangon', 'Asia/Yangon'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Australia/Canberra', 'Australia/Canberra'), ('Asia/Kabul', 'Asia/Kabul'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Asia/Atyrau', 'Asia/Atyrau'), ('GMT+0', 'GMT+0'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Africa/Kampala', 'Africa/Kampala'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Etc/UCT', 'Etc/UCT'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/Catamarca', 'America/Catamarca'), ('America/Winnipeg', 'America/Winnipeg'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Australia/Queensland', 'Australia/Queensland'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Europe/Athens', 'Europe/Athens'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Europe/Kirov', 'Europe/Kirov'), ('NZ-CHAT', 'NZ-CHAT'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Europe/Monaco', 'Europe/Monaco'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/St_Vincent', 'America/St_Vincent'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Yakutat', 'America/Yakutat'), ('US/Aleutian', 'US/Aleutian'), ('America/Cancun', 'America/Cancun'), ('Africa/Asmara', 'Africa/Asmara'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Jujuy', 'America/Jujuy'), ('America/Kralendijk', 'America/Kralendijk'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Grenada', 'America/Grenada'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Australia/West', 'Australia/West'), ('Asia/Kuwait', 'Asia/Kuwait'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Tijuana', 'America/Tijuana'), ('Africa/Maseru', 'Africa/Maseru'), ('Asia/Hovd', 'Asia/Hovd'), ('America/Knox_IN', 'America/Knox_IN'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Africa/Libreville', 'Africa/Libreville'), ('Kwajalein', 'Kwajalein'), ('US/Arizona', 'US/Arizona'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Etc/GMT-13', 'Etc/GMT-13'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('America/Sitka', 'America/Sitka'), ('Canada/Pacific', 'Canada/Pacific'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Asia/Almaty', 'Asia/Almaty'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Marigot', 'America/Marigot'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Tortola', 'America/Tortola'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('EST', 'EST'), ('Europe/Dublin', 'Europe/Dublin'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Beirut', 'Asia/Beirut'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Europe/Riga', 'Europe/Riga'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Canada/Yukon', 'Canada/Yukon'), ('Asia/Baku', 'Asia/Baku'), ('America/Cayenne', 'America/Cayenne'), ('PST8PDT', 'PST8PDT'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Mazatlan', 'America/Mazatlan'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Pacific/Efate', 'Pacific/Efate'), ('Indian/Mahe', 'Indian/Mahe'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Australia/Darwin', 'Australia/Darwin')], default='Europe/London', max_length=35),
        ),
    ]
