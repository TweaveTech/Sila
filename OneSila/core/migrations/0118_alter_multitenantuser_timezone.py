# Generated by Django 5.0.2 on 2024-07-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0117_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('America/St_Thomas', 'America/St_Thomas'), ('Brazil/East', 'Brazil/East'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Lima', 'America/Lima'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Asia/Dhaka', 'Asia/Dhaka'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Chihuahua', 'America/Chihuahua'), ('HST', 'HST'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Europe/Tirane', 'Europe/Tirane'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Shiprock', 'America/Shiprock'), ('America/Eirunepe', 'America/Eirunepe'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Juneau', 'America/Juneau'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('US/Mountain', 'US/Mountain'), ('America/Phoenix', 'America/Phoenix'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Africa/Harare', 'Africa/Harare'), ('Africa/Accra', 'Africa/Accra'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Regina', 'America/Regina'), ('America/Chicago', 'America/Chicago'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Bahia', 'America/Bahia'), ('Europe/Riga', 'Europe/Riga'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Africa/Lome', 'Africa/Lome'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Europe/Samara', 'Europe/Samara'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Asia/Beirut', 'Asia/Beirut'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Asia/Hebron', 'Asia/Hebron'), ('ROK', 'ROK'), ('Europe/Vatican', 'Europe/Vatican'), ('Europe/Brussels', 'Europe/Brussels'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Rainy_River', 'America/Rainy_River'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Australia/Eucla', 'Australia/Eucla'), ('Asia/Dili', 'Asia/Dili'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Africa/Blantyre', 'Africa/Blantyre'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Indian/Reunion', 'Indian/Reunion'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Manaus', 'America/Manaus'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Pacific/Kanton', 'Pacific/Kanton'), ('America/Atka', 'America/Atka'), ('Asia/Almaty', 'Asia/Almaty'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Iran', 'Iran'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Kuching', 'Asia/Kuching'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('US/Eastern', 'US/Eastern'), ('GB-Eire', 'GB-Eire'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Pacific/Palau', 'Pacific/Palau'), ('Etc/UCT', 'Etc/UCT'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Australia/Darwin', 'Australia/Darwin'), ('Brazil/Acre', 'Brazil/Acre'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Winnipeg', 'America/Winnipeg'), ('Asia/Macau', 'Asia/Macau'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Africa/Bamako', 'Africa/Bamako'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Australia/ACT', 'Australia/ACT'), ('America/Louisville', 'America/Louisville'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Asia/Amman', 'Asia/Amman'), ('EST5EDT', 'EST5EDT'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Europe/Monaco', 'Europe/Monaco'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Asia/Baku', 'Asia/Baku'), ('America/Montevideo', 'America/Montevideo'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Singapore', 'Asia/Singapore'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Detroit', 'America/Detroit'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Asia/Tehran', 'Asia/Tehran'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Chile/Continental', 'Chile/Continental'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Aqtau', 'Asia/Aqtau'), ('America/Tijuana', 'America/Tijuana'), ('GMT0', 'GMT0'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Moncton', 'America/Moncton'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Kashgar', 'Asia/Kashgar'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Montreal', 'America/Montreal'), ('Indian/Mahe', 'Indian/Mahe'), ('Europe/Budapest', 'Europe/Budapest'), ('Europe/London', 'Europe/London'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Hongkong', 'Hongkong'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Etc/Universal', 'Etc/Universal'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Asia/Harbin', 'Asia/Harbin'), ('NZ-CHAT', 'NZ-CHAT'), ('US/Hawaii', 'US/Hawaii'), ('America/Vancouver', 'America/Vancouver'), ('GMT+0', 'GMT+0'), ('Africa/Douala', 'Africa/Douala'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Monterrey', 'America/Monterrey'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('GMT', 'GMT'), ('America/Guatemala', 'America/Guatemala'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Lagos', 'Africa/Lagos'), ('Pacific/Apia', 'Pacific/Apia'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Greenwich', 'Greenwich'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Yellowknife', 'America/Yellowknife'), ('Canada/Central', 'Canada/Central'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('America/Inuvik', 'America/Inuvik'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Europe/San_Marino', 'Europe/San_Marino'), ('America/Edmonton', 'America/Edmonton'), ('America/Mazatlan', 'America/Mazatlan'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Nassau', 'America/Nassau'), ('America/Cancun', 'America/Cancun'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('America/Jujuy', 'America/Jujuy'), ('CST6CDT', 'CST6CDT'), ('America/Whitehorse', 'America/Whitehorse'), ('America/St_Vincent', 'America/St_Vincent'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Dominica', 'America/Dominica'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Toronto', 'America/Toronto'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Navajo', 'Navajo'), ('America/Catamarca', 'America/Catamarca'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Factory', 'Factory'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Atikokan', 'America/Atikokan'), ('Asia/Muscat', 'Asia/Muscat'), ('GB', 'GB'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Australia/South', 'Australia/South'), ('Jamaica', 'Jamaica'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Europe/Zurich', 'Europe/Zurich'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Australia/West', 'Australia/West'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('America/Boise', 'America/Boise'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Belize', 'America/Belize'), ('America/Halifax', 'America/Halifax'), ('PRC', 'PRC'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Asia/Omsk', 'Asia/Omsk'), ('Universal', 'Universal'), ('America/Grenada', 'America/Grenada'), ('Asia/Shanghai', 'Asia/Shanghai'), ('US/Michigan', 'US/Michigan'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Metlakatla', 'America/Metlakatla'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Paramaribo', 'America/Paramaribo'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Nipigon', 'America/Nipigon'), ('America/Guayaquil', 'America/Guayaquil'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Etc/GMT+3', 'Etc/GMT+3'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Asia/Makassar', 'Asia/Makassar'), ('America/Santarem', 'America/Santarem'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Europe/Prague', 'Europe/Prague'), ('Africa/Maputo', 'Africa/Maputo'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('UCT', 'UCT'), ('America/Merida', 'America/Merida'), ('Africa/Bangui', 'Africa/Bangui'), ('America/St_Lucia', 'America/St_Lucia'), ('America/Matamoros', 'America/Matamoros'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Africa/Dakar', 'Africa/Dakar'), ('America/St_Johns', 'America/St_Johns'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Israel', 'Israel'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Nome', 'America/Nome'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Yakutat', 'America/Yakutat'), ('America/Cayenne', 'America/Cayenne'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Australia/Perth', 'Australia/Perth'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Etc/GMT', 'Etc/GMT'), ('America/Asuncion', 'America/Asuncion'), ('Europe/Malta', 'Europe/Malta'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Africa/Juba', 'Africa/Juba'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('US/Alaska', 'US/Alaska'), ('Asia/Colombo', 'Asia/Colombo'), ('Australia/NSW', 'Australia/NSW'), ('America/Virgin', 'America/Virgin'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Sitka', 'America/Sitka'),
                                   ('Asia/Chungking', 'Asia/Chungking'), ('Kwajalein', 'Kwajalein'), ('America/Godthab', 'America/Godthab'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Montserrat', 'America/Montserrat'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Asia/Oral', 'Asia/Oral'), ('Africa/Tunis', 'Africa/Tunis'), ('Asia/Gaza', 'Asia/Gaza'), ('Europe/Paris', 'Europe/Paris'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Creston', 'America/Creston'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Adak', 'America/Adak'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Guyana', 'America/Guyana'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Europe/Skopje', 'Europe/Skopje'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('MST7MDT', 'MST7MDT'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Australia/Victoria', 'Australia/Victoria'), ('US/Arizona', 'US/Arizona'), ('NZ', 'NZ'), ('Europe/Busingen', 'Europe/Busingen'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Asia/Magadan', 'Asia/Magadan'), ('Asia/Nicosia', 'Asia/Nicosia'), ('MST', 'MST'), ('Egypt', 'Egypt'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Tomsk', 'Asia/Tomsk'), ('America/Denver', 'America/Denver'), ('America/Resolute', 'America/Resolute'), ('Asia/Macao', 'Asia/Macao'), ('America/Caracas', 'America/Caracas'), ('America/Thule', 'America/Thule'), ('Europe/Rome', 'Europe/Rome'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Europe/Athens', 'Europe/Athens'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Pacific/Midway', 'Pacific/Midway'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Mexico_City', 'America/Mexico_City'), ('America/Panama', 'America/Panama'), ('America/Curacao', 'America/Curacao'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Nuuk', 'America/Nuuk'), ('Etc/GMT-0', 'Etc/GMT-0'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Australia/Currie', 'Australia/Currie'), ('Australia/Queensland', 'Australia/Queensland'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Africa/Luanda', 'Africa/Luanda'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Europe/Jersey', 'Europe/Jersey'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Asmara', 'Africa/Asmara'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Asia/Dacca', 'Asia/Dacca'), ('GMT-0', 'GMT-0'), ('Africa/Libreville', 'Africa/Libreville'), ('EET', 'EET'), ('Indian/Comoro', 'Indian/Comoro'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Aruba', 'America/Aruba'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Yangon', 'Asia/Yangon'), ('Europe/Oslo', 'Europe/Oslo'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Libya', 'Libya'), ('America/Santiago', 'America/Santiago'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Africa/Kigali', 'Africa/Kigali'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('US/Pacific', 'US/Pacific'), ('America/Cayman', 'America/Cayman'), ('Asia/Taipei', 'Asia/Taipei'), ('Africa/Niamey', 'Africa/Niamey'), ('Australia/Canberra', 'Australia/Canberra'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Africa/Kampala', 'Africa/Kampala'), ('Asia/Kabul', 'Asia/Kabul'), ('America/New_York', 'America/New_York'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/Noronha', 'America/Noronha'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Dawson', 'America/Dawson'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Anguilla', 'America/Anguilla'), ('America/St_Kitts', 'America/St_Kitts'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Australia/Sydney', 'Australia/Sydney'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Asia/Vientiane', 'Asia/Vientiane'), ('W-SU', 'W-SU'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Portugal', 'Portugal'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Pacific/Yap', 'Pacific/Yap'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Anchorage', 'America/Anchorage'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Turkey', 'Turkey'), ('America/Bogota', 'America/Bogota'), ('Europe/Madrid', 'Europe/Madrid'), ('Iceland', 'Iceland'), ('US/Samoa', 'US/Samoa'), ('Africa/Cairo', 'Africa/Cairo'), ('Africa/Algiers', 'Africa/Algiers'), ('Pacific/Efate', 'Pacific/Efate'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Managua', 'America/Managua'), ('EST', 'EST'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Africa/Malabo', 'Africa/Malabo'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Marigot', 'America/Marigot'), ('America/Recife', 'America/Recife'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Menominee', 'America/Menominee'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Kralendijk', 'America/Kralendijk'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Europe/Berlin', 'Europe/Berlin'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Indian/Cocos', 'Indian/Cocos'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Japan', 'Japan'), ('America/Ensenada', 'America/Ensenada'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Cuba', 'Cuba'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Havana', 'America/Havana'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Europe/Minsk', 'Europe/Minsk'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Eire', 'Eire'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Martinique', 'America/Martinique'), ('MET', 'MET'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Belem', 'America/Belem'), ('Canada/Pacific', 'Canada/Pacific'), ('Europe/Moscow', 'Europe/Moscow'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Maceio', 'America/Maceio'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Africa/Freetown', 'Africa/Freetown'), ('Asia/Brunei', 'Asia/Brunei'), ('America/Jamaica', 'America/Jamaica'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Africa/Bissau', 'Africa/Bissau'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Manila', 'Asia/Manila'), ('Indian/Christmas', 'Indian/Christmas'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Dubai', 'Asia/Dubai'), ('Asia/Tokyo', 'Asia/Tokyo'), ('US/Central', 'US/Central'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('America/Swift_Current', 'America/Swift_Current'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Europe/Andorra', 'Europe/Andorra'), ('Asia/Aden', 'Asia/Aden'), ('US/East-Indiana', 'US/East-Indiana'), ('build/etc/localtime', 'build/etc/localtime'), ('ROC', 'ROC'), ('Poland', 'Poland'), ('Indian/Maldives', 'Indian/Maldives'), ('America/Tortola', 'America/Tortola'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Europe/Sofia', 'Europe/Sofia'), ('America/La_Paz', 'America/La_Paz'), ('Asia/Saigon', 'Asia/Saigon'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Rosario', 'America/Rosario'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Mendoza', 'America/Mendoza'), ('Europe/Dublin', 'Europe/Dublin'), ('Etc/GMT-10', 'Etc/GMT-10'), ('US/Aleutian', 'US/Aleutian'), ('Brazil/West', 'Brazil/West'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Asia/Damascus', 'Asia/Damascus'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('WET', 'WET'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Miquelon', 'America/Miquelon'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Europe/Nicosia', 'Europe/Nicosia'), ('CET', 'CET'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Indianapolis', 'America/Indianapolis'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Australia/Hobart', 'Australia/Hobart'), ('PST8PDT', 'PST8PDT'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Zulu', 'Zulu'), ('Australia/North', 'Australia/North'), ('Etc/UTC', 'Etc/UTC'), ('America/Cuiaba', 'America/Cuiaba'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Pacific/Easter', 'Pacific/Easter'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Asia/Bishkek', 'Asia/Bishkek'), ('UTC', 'UTC'), ('Singapore', 'Singapore'), ('Asia/Hovd', 'Asia/Hovd'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Mexico/General', 'Mexico/General'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Antigua', 'America/Antigua'), ('Asia/Chita', 'Asia/Chita'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Australia/LHI', 'Australia/LHI'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Barbados', 'America/Barbados'), ('Europe/Guernsey', 'Europe/Guernsey')], default='Europe/London', max_length=35),
        ),
    ]
