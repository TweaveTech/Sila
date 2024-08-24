# Generated by Django 5.0.2 on 2024-05-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Europe/Kirov', 'Europe/Kirov'), ('America/Anguilla', 'America/Anguilla'), ('America/Boa_Vista', 'America/Boa_Vista'), ('America/Miquelon', 'America/Miquelon'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Europe/Minsk', 'Europe/Minsk'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Mazatlan', 'America/Mazatlan'), ('Etc/GMT', 'Etc/GMT'), ('Europe/Belfast', 'Europe/Belfast'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Rainy_River', 'America/Rainy_River'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Phoenix', 'America/Phoenix'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Accra', 'Africa/Accra'), ('Europe/Athens', 'Europe/Athens'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('HST', 'HST'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Etc/GMT0', 'Etc/GMT0'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Europe/Busingen', 'Europe/Busingen'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Brazil/West', 'Brazil/West'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Etc/UTC', 'Etc/UTC'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Asuncion', 'America/Asuncion'), ('Brazil/East', 'Brazil/East'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Africa/Libreville', 'Africa/Libreville'), ('America/Cancun', 'America/Cancun'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Mexico_City', 'America/Mexico_City'), ('Asia/Macau', 'Asia/Macau'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Australia/Victoria', 'Australia/Victoria'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/Iqaluit', 'America/Iqaluit'), ('Israel', 'Israel'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Portugal', 'Portugal'), ('America/Martinique', 'America/Martinique'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Atlantic/Azores', 'Atlantic/Azores'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/Aruba', 'America/Aruba'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Africa/Bamako', 'Africa/Bamako'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Asia/Kabul', 'Asia/Kabul'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Japan', 'Japan'), ('Chile/Continental', 'Chile/Continental'), ('Europe/Moscow', 'Europe/Moscow'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Africa/Banjul', 'Africa/Banjul'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Etc/GMT+6', 'Etc/GMT+6'), ('US/Samoa', 'US/Samoa'), ('America/Chicago', 'America/Chicago'), ('Europe/Paris', 'Europe/Paris'), ('America/Virgin', 'America/Virgin'), ('PRC', 'PRC'), ('CET', 'CET'), ('America/Marigot', 'America/Marigot'), ('Mexico/General', 'Mexico/General'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('WET', 'WET'), ('America/St_Lucia', 'America/St_Lucia'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Asia/Damascus', 'Asia/Damascus'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Europe/Monaco', 'Europe/Monaco'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Asia/Macao', 'Asia/Macao'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Merida', 'America/Merida'), ('GMT0', 'GMT0'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Dawson', 'America/Dawson'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Curacao', 'America/Curacao'), ('Africa/Lagos', 'Africa/Lagos'), ('Asia/Amman', 'Asia/Amman'), ('Eire', 'Eire'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Brazil/Acre', 'Brazil/Acre'), ('US/Mountain', 'US/Mountain'), ('Zulu', 'Zulu'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Africa/Freetown', 'Africa/Freetown'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Knox_IN', 'America/Knox_IN'), ('Europe/Kiev', 'Europe/Kiev'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Ensenada', 'America/Ensenada'), ('Asia/Almaty', 'Asia/Almaty'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Montreal', 'America/Montreal'), ('America/New_York', 'America/New_York'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Panama', 'America/Panama'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('US/Hawaii', 'US/Hawaii'), ('Australia/Currie', 'Australia/Currie'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Louisville', 'America/Louisville'), ('Canada/Central', 'Canada/Central'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Africa/Asmera', 'Africa/Asmera'), ('US/Arizona', 'US/Arizona'), ('America/Caracas', 'America/Caracas'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Europe/Oslo', 'Europe/Oslo'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Australia/LHI', 'Australia/LHI'), ('Africa/Kampala', 'Africa/Kampala'), ('America/Metlakatla', 'America/Metlakatla'), ('Europe/Tirane', 'Europe/Tirane'), ('Australia/Hobart', 'Australia/Hobart'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Guayaquil', 'America/Guayaquil'), ('Singapore', 'Singapore'), ('Africa/Douala', 'Africa/Douala'), ('America/Godthab', 'America/Godthab'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Thule', 'America/Thule'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Antigua', 'America/Antigua'), ('America/Manaus', 'America/Manaus'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Australia/ACT', 'Australia/ACT'), ('Europe/Saratov', 'Europe/Saratov'), ('Europe/Dublin', 'Europe/Dublin'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('ROK', 'ROK'), ('Hongkong', 'Hongkong'), ('Asia/Oral', 'Asia/Oral'), ('Europe/Malta', 'Europe/Malta'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Europe/Rome', 'Europe/Rome'), ('UTC', 'UTC'), ('US/Pacific', 'US/Pacific'), ('Indian/Maldives', 'Indian/Maldives'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Denver', 'America/Denver'), ('US/Central', 'US/Central'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Europe/Zurich', 'Europe/Zurich'), ('Australia/North', 'Australia/North'), ('America/Montevideo', 'America/Montevideo'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Lima', 'America/Lima'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Pacific/Truk', 'Pacific/Truk'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Europe/Riga', 'Europe/Riga'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Santarem', 'America/Santarem'), ('US/Eastern', 'US/Eastern'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('GB-Eire', 'GB-Eire'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Europe/Vienna', 'Europe/Vienna'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Makassar', 'Asia/Makassar'), ('America/Atka', 'America/Atka'), ('America/Menominee', 'America/Menominee'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Africa/Lome', 'Africa/Lome'), ('Pacific/Midway', 'Pacific/Midway'), ('America/Cayman', 'America/Cayman'), ('Europe/Skopje', 'Europe/Skopje'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Indian/Comoro', 'Indian/Comoro'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Regina', 'America/Regina'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Europe/Budapest', 'Europe/Budapest'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Asia/Saigon', 'Asia/Saigon'), ('Etc/GMT+3', 'Etc/GMT+3'), ('MST7MDT', 'MST7MDT'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Montserrat', 'America/Montserrat'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Noronha', 'America/Noronha'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Shiprock', 'America/Shiprock'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Jersey', 'Europe/Jersey'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('America/Maceio', 'America/Maceio'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Tortola', 'America/Tortola'), ('America/Halifax', 'America/Halifax'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Jamaica', 'America/Jamaica'), ('America/Monterrey', 'America/Monterrey'), ('Australia/NSW', 'Australia/NSW'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Recife', 'America/Recife'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Moncton', 'America/Moncton'), ('PST8PDT', 'PST8PDT'), ('America/St_Kitts',
                                   'America/St_Kitts'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Etc/Zulu', 'Etc/Zulu'), ('Africa/Malabo', 'Africa/Malabo'), ('CST6CDT', 'CST6CDT'), ('America/Paramaribo', 'America/Paramaribo'), ('Asia/Singapore', 'Asia/Singapore'), ('Pacific/Easter', 'Pacific/Easter'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Etc/UCT', 'Etc/UCT'), ('build/etc/localtime', 'build/etc/localtime'), ('America/Guatemala', 'America/Guatemala'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('America/St_Thomas', 'America/St_Thomas'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Rangoon', 'Asia/Rangoon'), ('NZ', 'NZ'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Navajo', 'Navajo'), ('Asia/Chita', 'Asia/Chita'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/Creston', 'America/Creston'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Los_Angeles', 'America/Los_Angeles'), ('America/Sitka', 'America/Sitka'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Australia/South', 'Australia/South'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Australia/Perth', 'Australia/Perth'), ('Asia/Beirut', 'Asia/Beirut'), ('Pacific/Johnston', 'Pacific/Johnston'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Resolute', 'America/Resolute'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Bogota', 'America/Bogota'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Winnipeg', 'America/Winnipeg'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Europe/Madrid', 'Europe/Madrid'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Inuvik', 'America/Inuvik'), ('GMT+0', 'GMT+0'), ('Australia/Eucla', 'Australia/Eucla'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Indian/Mahe', 'Indian/Mahe'), ('Cuba', 'Cuba'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Europe/Andorra', 'Europe/Andorra'), ('GB', 'GB'), ('Indian/Christmas', 'Indian/Christmas'), ('America/La_Paz', 'America/La_Paz'), ('America/Swift_Current', 'America/Swift_Current'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Santiago', 'America/Santiago'), ('Pacific/Palau', 'Pacific/Palau'), ('America/St_Vincent', 'America/St_Vincent'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Baku', 'Asia/Baku'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Asia/Kuching', 'Asia/Kuching'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Africa/Algiers', 'Africa/Algiers'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Asia/Manila', 'Asia/Manila'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Eirunepe', 'America/Eirunepe'), ('Asia/Karachi', 'Asia/Karachi'), ('ROC', 'ROC'), ('Jamaica', 'Jamaica'), ('Asia/Seoul', 'Asia/Seoul'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Campo_Grande', 'America/Campo_Grande'), ('America/Chihuahua', 'America/Chihuahua'), ('Pacific/Niue', 'Pacific/Niue'), ('Africa/Conakry', 'Africa/Conakry'), ('Africa/Harare', 'Africa/Harare'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Boise', 'America/Boise'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Africa/Bangui', 'Africa/Bangui'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Poland', 'Poland'), ('Europe/London', 'Europe/London'), ('Factory', 'Factory'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Pacific/Yap', 'Pacific/Yap'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Asia/Taipei', 'Asia/Taipei'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Asia/Brunei', 'Asia/Brunei'), ('America/Detroit', 'America/Detroit'), ('America/Juneau', 'America/Juneau'), ('MST', 'MST'), ('America/Nipigon', 'America/Nipigon'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('NZ-CHAT', 'NZ-CHAT'), ('US/Michigan', 'US/Michigan'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Asia/Kolkata', 'Asia/Kolkata'), ('GMT', 'GMT'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Etc/GMT+2', 'Etc/GMT+2'), ('EET', 'EET'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('MET', 'MET'), ('America/Guyana', 'America/Guyana'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Africa/Cairo', 'Africa/Cairo'), ('America/Nome', 'America/Nome'), ('Canada/Pacific', 'Canada/Pacific'), ('W-SU', 'W-SU'), ('America/Cayenne', 'America/Cayenne'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Asia/Aden', 'Asia/Aden'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('US/Aleutian', 'US/Aleutian'), ('Iceland', 'Iceland'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Yakutat', 'America/Yakutat'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Africa/Kigali', 'Africa/Kigali'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Yellowknife', 'America/Yellowknife'), ('Pacific/Efate', 'Pacific/Efate'), ('Greenwich', 'Greenwich'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Africa/Asmara', 'Africa/Asmara'), ('Asia/Pontianak', 'Asia/Pontianak'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Pacific/Guam', 'Pacific/Guam'), ('Kwajalein', 'Kwajalein'), ('America/Nassau', 'America/Nassau'), ('America/Cuiaba', 'America/Cuiaba'), ('Egypt', 'Egypt'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Australia/West', 'Australia/West'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Belize', 'America/Belize'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Australia/Darwin', 'Australia/Darwin'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Belem', 'America/Belem'), ('Antarctica/Casey', 'Antarctica/Casey'), ('UCT', 'UCT'), ('Europe/Prague', 'Europe/Prague'), ('Europe/Samara', 'Europe/Samara'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/St_Johns', 'America/St_Johns'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Yangon', 'Asia/Yangon'), ('EST5EDT', 'EST5EDT'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Havana', 'America/Havana'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Universal', 'Universal'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Rosario', 'America/Rosario'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Asia/Hebron', 'Asia/Hebron'), ('America/Toronto', 'America/Toronto'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Kralendijk', 'America/Kralendijk'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Tijuana', 'America/Tijuana'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('America/Hermosillo', 'America/Hermosillo'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Asia/Dili', 'Asia/Dili'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Managua', 'America/Managua'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Australia/Queensland', 'Australia/Queensland'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Turkey', 'Turkey'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Jujuy', 'America/Jujuy'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Asia/Chungking', 'Asia/Chungking'), ('Africa/Juba', 'Africa/Juba'), ('America/El_Salvador', 'America/El_Salvador'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Iran', 'Iran'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Africa/Tunis', 'Africa/Tunis'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Cordoba', 'America/Cordoba'), ('America/Vancouver', 'America/Vancouver'), ('America/Barbados', 'America/Barbados'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Atikokan', 'America/Atikokan'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('EST', 'EST'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Libya', 'Libya'), ('Asia/Nicosia', 'Asia/Nicosia'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('GMT-0', 'GMT-0'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Grenada', 'America/Grenada'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Bahia', 'America/Bahia'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Pacific/Wake', 'Pacific/Wake'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Adak', 'America/Adak'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Asia/Colombo', 'Asia/Colombo'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('America/Anchorage', 'America/Anchorage'), ('America/Catamarca', 'America/Catamarca'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Asia/Harbin', 'Asia/Harbin'), ('Australia/Adelaide', 'Australia/Adelaide'), ('America/Matamoros', 'America/Matamoros'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Asia/Muscat', 'Asia/Muscat'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('US/Alaska', 'US/Alaska'), ('America/Mendoza', 'America/Mendoza'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Dominica', 'America/Dominica')], default='Europe/London', max_length=35),
        ),
    ]
