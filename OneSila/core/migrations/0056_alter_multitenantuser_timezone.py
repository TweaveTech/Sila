# Generated by Django 5.0.2 on 2024-05-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('America/Eirunepe', 'America/Eirunepe'), ('America/Ensenada', 'America/Ensenada'), ('America/Noronha', 'America/Noronha'), ('America/Halifax', 'America/Halifax'), ('Universal', 'Universal'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Damascus', 'Asia/Damascus'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Australia/North', 'Australia/North'), ('Zulu', 'Zulu'), ('America/Paramaribo', 'America/Paramaribo'), ('Pacific/Yap', 'Pacific/Yap'), ('Africa/Cairo', 'Africa/Cairo'), ('Asia/Tehran', 'Asia/Tehran'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Tijuana', 'America/Tijuana'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('NZ', 'NZ'), ('America/Resolute', 'America/Resolute'), ('America/Adak', 'America/Adak'), ('Asia/Makassar', 'Asia/Makassar'), ('Europe/Moscow', 'Europe/Moscow'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Guayaquil', 'America/Guayaquil'), ('Asia/Aden', 'Asia/Aden'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Asia/Taipei', 'Asia/Taipei'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Atka', 'America/Atka'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Etc/UCT', 'Etc/UCT'), ('America/Nipigon', 'America/Nipigon'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Anchorage', 'America/Anchorage'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Bahia', 'America/Bahia'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Chile/Continental', 'Chile/Continental'), ('Brazil/East', 'Brazil/East'), ('Asia/Manila', 'Asia/Manila'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Greenwich', 'Greenwich'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Australia/Eucla', 'Australia/Eucla'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Mazatlan', 'America/Mazatlan'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Santarem', 'America/Santarem'), ('America/Jamaica', 'America/Jamaica'), ('Etc/GMT+3', 'Etc/GMT+3'), ('US/Samoa', 'US/Samoa'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Grenada', 'America/Grenada'), ('America/Sitka', 'America/Sitka'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Europe/Tirane', 'Europe/Tirane'), ('Asia/Colombo', 'Asia/Colombo'), ('Asia/Baku', 'Asia/Baku'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Europe/Saratov', 'Europe/Saratov'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Israel', 'Israel'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Iceland', 'Iceland'), ('Europe/Prague', 'Europe/Prague'), ('Asia/Omsk', 'Asia/Omsk'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Australia/Hobart', 'Australia/Hobart'), ('Africa/Juba', 'Africa/Juba'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('US/Mountain', 'US/Mountain'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Antigua', 'America/Antigua'), ('America/Montreal', 'America/Montreal'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Africa/Tunis', 'Africa/Tunis'), ('America/St_Thomas', 'America/St_Thomas'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Australia/Sydney', 'Australia/Sydney'), ('Africa/Banjul', 'Africa/Banjul'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Iqaluit', 'America/Iqaluit'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Bogota', 'America/Bogota'), ('America/Guyana', 'America/Guyana'), ('America/Moncton', 'America/Moncton'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Knox_IN', 'America/Knox_IN'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Poland', 'Poland'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Asia/Magadan', 'Asia/Magadan'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Canada/Eastern', 'Canada/Eastern'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Belem', 'America/Belem'), ('America/Catamarca', 'America/Catamarca'), ('America/Montserrat', 'America/Montserrat'), ('US/Arizona', 'US/Arizona'), ('US/Alaska', 'US/Alaska'), ('Asia/Muscat', 'Asia/Muscat'), ('UTC', 'UTC'), ('America/La_Paz', 'America/La_Paz'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Africa/Dakar', 'Africa/Dakar'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Antarctica/Casey', 'Antarctica/Casey'), ('America/Cayenne', 'America/Cayenne'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Europe/Stockholm', 'Europe/Stockholm'), ('NZ-CHAT', 'NZ-CHAT'), ('Europe/Riga', 'Europe/Riga'), ('America/Santiago', 'America/Santiago'), ('America/Cordoba', 'America/Cordoba'), ('Australia/ACT', 'Australia/ACT'), ('Africa/Luanda', 'Africa/Luanda'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Africa/Asmara', 'Africa/Asmara'), ('Europe/Rome', 'Europe/Rome'), ('Asia/Brunei', 'Asia/Brunei'), ('Australia/West', 'Australia/West'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Havana', 'America/Havana'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Australia/Victoria', 'Australia/Victoria'), ('Canada/Pacific', 'Canada/Pacific'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Juneau', 'America/Juneau'), ('Pacific/Efate', 'Pacific/Efate'), ('US/Pacific', 'US/Pacific'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Whitehorse', 'America/Whitehorse'), ('America/St_Kitts', 'America/St_Kitts'), ('Asia/Seoul', 'Asia/Seoul'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Europe/Samara', 'Europe/Samara'), ('Europe/Dublin', 'Europe/Dublin'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/St_Lucia', 'America/St_Lucia'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Etc/GMT+5', 'Etc/GMT+5'), ('US/Eastern', 'US/Eastern'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Libreville', 'Africa/Libreville'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Navajo', 'Navajo'), ('America/Guatemala', 'America/Guatemala'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('EST5EDT', 'EST5EDT'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Inuvik', 'America/Inuvik'), ('America/St_Vincent', 'America/St_Vincent'), ('GB', 'GB'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Phoenix', 'America/Phoenix'), ('Europe/Belfast', 'Europe/Belfast'), ('Australia/LHI', 'Australia/LHI'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Vancouver', 'America/Vancouver'), ('Europe/Kiev', 'Europe/Kiev'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Costa_Rica', 'America/Costa_Rica'), ('US/Aleutian', 'US/Aleutian'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('US/East-Indiana', 'US/East-Indiana'), ('CET', 'CET'), ('America/Detroit', 'America/Detroit'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Jamaica', 'Jamaica'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Denver', 'America/Denver'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Europe/Zurich', 'Europe/Zurich'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Pacific/Ponape', 'Pacific/Ponape'), ('ROK', 'ROK'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Asuncion', 'America/Asuncion'), ('America/Mexico_City', 'America/Mexico_City'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Toronto', 'America/Toronto'), ('US/Michigan', 'US/Michigan'), ('Asia/Karachi', 'Asia/Karachi'), ('Asia/Macao', 'Asia/Macao'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Australia/Queensland', 'Australia/Queensland'), ('America/Rosario', 'America/Rosario'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Los_Angeles', 'America/Los_Angeles'), ('UCT', 'UCT'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Cancun', 'America/Cancun'), ('Indian/Mahe', 'Indian/Mahe'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Asia/Singapore', 'Asia/Singapore'), ('W-SU', 'W-SU'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Indian/Cocos', 'Indian/Cocos'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Africa/Malabo', 'Africa/Malabo'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Africa/Casablanca', 'Africa/Casablanca'), ('America/Martinique', 'America/Martinique'), ('America/Barbados', 'America/Barbados'), ('America/Nassau', 'America/Nassau'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Thule', 'America/Thule'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Asia/Tashkent', 'Asia/Tashkent'), ('GMT', 'GMT'), ('Asia/Yangon', 'Asia/Yangon'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Turkey', 'Turkey'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Africa/Douala', 'Africa/Douala'), ('America/Shiprock', 'America/Shiprock'), ('Europe/Vienna', 'Europe/Vienna'), ('Japan', 'Japan'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Etc/GMT', 'Etc/GMT'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Africa/Niamey', 'Africa/Niamey'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Asia/Dubai', 'Asia/Dubai'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Africa/Kigali', 'Africa/Kigali'), ('Pacific/Johnston', 'Pacific/Johnston'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Asia/Harbin', 'Asia/Harbin'), ('Mexico/General', 'Mexico/General'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Africa/Freetown', 'Africa/Freetown'), ('Asia/Saigon', 'Asia/Saigon'), ('GMT0', 'GMT0'), ('build/etc/localtime', 'build/etc/localtime'), ('Asia/Oral', 'Asia/Oral'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('US/Hawaii', 'US/Hawaii'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Europe/Sofia', 'Europe/Sofia'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Europe/Madrid', 'Europe/Madrid'), ('CST6CDT', 'CST6CDT'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Jujuy', 'America/Jujuy'), ('Europe/Busingen', 'Europe/Busingen'), ('America/St_Johns', 'America/St_Johns'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Africa/Conakry', 'Africa/Conakry'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Europe/Brussels', 'Europe/Brussels'), ('Portugal', 'Portugal'), ('America/Menominee', 'America/Menominee'), ('Asia/Nicosia', 'Asia/Nicosia'), ('America/Mendoza', 'America/Mendoza'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Indian/Maldives', 'Indian/Maldives'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Australia/Darwin', 'Australia/Darwin'), ('America/Maceio', 'America/Maceio'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Asia/Kuching', 'Asia/Kuching'), ('WET', 'WET'), ('America/New_York', 'America/New_York'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Etc/GMT-5', 'Etc/GMT-5'), ('GMT-0', 'GMT-0'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Panama', 'America/Panama'), ('America/Matamoros', 'America/Matamoros'), ('Canada/Yukon', 'Canada/Yukon'), ('Indian/Comoro', 'Indian/Comoro'), ('MET', 'MET'), ('America/Atikokan', 'America/Atikokan'), ('MST7MDT', 'MST7MDT'), ('Pacific/Wake', 'Pacific/Wake'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Pacific/Auckland', 'Pacific/Auckland'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Metlakatla', 'America/Metlakatla'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Winnipeg', 'America/Winnipeg'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Africa/Maseru', 'Africa/Maseru'), ('PRC', 'PRC'), ('America/Dominica', 'America/Dominica'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Chicago', 'America/Chicago'), ('Asia/Macau', 'Asia/Macau'), ('Europe/London', 'Europe/London'), ('EST', 'EST'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Etc/UTC', 'Etc/UTC'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Africa/Lagos', 'Africa/Lagos'), ('America/Caracas', 'America/Caracas'), ('PST8PDT', 'PST8PDT'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Godthab', 'America/Godthab'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Regina', 'America/Regina'), ('MST', 'MST'), ('Africa/Bamako', 'Africa/Bamako'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Etc/Zulu', 'Etc/Zulu'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Dawson', 'America/Dawson'), ('Iran', 'Iran'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Pacific/Niue', 'Pacific/Niue'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Yakutat', 'America/Yakutat'), ('Europe/Malta', 'Europe/Malta'), ('Kwajalein', 'Kwajalein'), ('Etc/Universal', 'Etc/Universal'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('ROC', 'ROC'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Africa/Bangui', 'Africa/Bangui'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Africa/Bissau', 'Africa/Bissau'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Anguilla', 'America/Anguilla'), ('America/Creston', 'America/Creston'), ('Europe/Jersey', 'Europe/Jersey'), ('Singapore', 'Singapore'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('GB-Eire', 'GB-Eire'), ('America/Belize', 'America/Belize'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Australia/Perth', 'Australia/Perth'), ('America/Cayman', 'America/Cayman'), ('Asia/Hovd', 'Asia/Hovd'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Africa/Accra', 'Africa/Accra'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Nuuk', 'America/Nuuk'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Hebron', 'Asia/Hebron'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Australia/NSW', 'Australia/NSW'), ('America/Kralendijk', 'America/Kralendijk'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Libya', 'Libya'), ('America/Marigot', 'America/Marigot'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Australia/South', 'Australia/South'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Europe/Monaco', 'Europe/Monaco'), ('America/Swift_Current', 'America/Swift_Current'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Africa/Maputo', 'Africa/Maputo'), ('America/El_Salvador', 'America/El_Salvador'), ('GMT+0', 'GMT+0'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Manaus', 'America/Manaus'), ('Pacific/Kanton', 'Pacific/Kanton'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Indianapolis', 'America/Indianapolis'), ('Asia/Beirut', 'Asia/Beirut'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Factory', 'Factory'), ('Pacific/Apia', 'Pacific/Apia'), ('Etc/GMT-0', 'Etc/GMT-0'), ('America/Virgin', 'America/Virgin'), ('America/Managua', 'America/Managua'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Pacific/Easter', 'Pacific/Easter'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Rainy_River', 'America/Rainy_River'), ('Hongkong', 'Hongkong'), ('Canada/Central', 'Canada/Central'), ('Africa/Lome', 'Africa/Lome'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/Yellowknife', 'America/Yellowknife'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Asia/Amman', 'Asia/Amman'), ('US/Central', 'US/Central'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Miquelon', 'America/Miquelon'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Europe/Paris', 'Europe/Paris'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Pacific/Palau', 'Pacific/Palau'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Africa/Kampala', 'Africa/Kampala'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('EET', 'EET'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Egypt', 'Egypt'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Merida', 'America/Merida'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Recife', 'America/Recife'), ('Cuba', 'Cuba'), ('America/Nome', 'America/Nome'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Montevideo', 'America/Montevideo'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Brazil/Acre', 'Brazil/Acre'), ('Europe/Athens', 'Europe/Athens'), ('America/Curacao', 'America/Curacao'), ('America/Louisville', 'America/Louisville'), ('HST', 'HST'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Monterrey', 'America/Monterrey'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Asia/Istanbul', 'Asia/Istanbul'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Africa/Harare', 'Africa/Harare'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Europe/Kirov', 'Europe/Kirov'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Dili', 'Asia/Dili'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Europe/Minsk', 'Europe/Minsk'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Brazil/West', 'Brazil/West'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Eire', 'Eire'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Aruba', 'America/Aruba'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Asia/Chita', 'Asia/Chita'), ('America/Boise', 'America/Boise'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Lima', 'America/Lima'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Tortola', 'America/Tortola'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Pacific/Guam', 'Pacific/Guam'), ('Africa/Mbabane', 'Africa/Mbabane')], default='Europe/London', max_length=35),
        ),
    ]
