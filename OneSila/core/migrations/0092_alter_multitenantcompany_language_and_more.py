# Generated by Django 5.0.2 on 2024-06-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantcompany',
            name='language',
            field=models.CharField(choices=[('nl', 'Nederlands'), ('en', 'English'), ('en-gb', 'English GB')], default='en', max_length=7),
        ),
        migrations.AlterField(
            model_name='multitenantuser',
            name='language',
            field=models.CharField(choices=[('nl', 'Nederlands'), ('en', 'English'), ('en-gb', 'English GB')], default='en', max_length=7),
        ),
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Europe/Lisbon', 'Europe/Lisbon'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Inuvik', 'America/Inuvik'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Kwajalein', 'Kwajalein'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Australia/NSW', 'Australia/NSW'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Moncton', 'America/Moncton'), ('Pacific/Yap', 'Pacific/Yap'), ('Asia/Magadan', 'Asia/Magadan'), ('Europe/Dublin', 'Europe/Dublin'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Detroit', 'America/Detroit'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Bahia', 'America/Bahia'), ('PRC', 'PRC'), ('America/Catamarca', 'America/Catamarca'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Merida', 'America/Merida'), ('America/Yellowknife', 'America/Yellowknife'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Asia/Damascus', 'Asia/Damascus'), ('Asia/Chungking', 'Asia/Chungking'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Miquelon', 'America/Miquelon'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Asia/Makassar', 'Asia/Makassar'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Cancun', 'America/Cancun'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Montreal', 'America/Montreal'), ('CET', 'CET'), ('America/Eirunepe', 'America/Eirunepe'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/Winnipeg', 'America/Winnipeg'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Europe/Jersey', 'Europe/Jersey'), ('America/Knox_IN', 'America/Knox_IN'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Guadeloupe', 'America/Guadeloupe'), ('US/Eastern', 'US/Eastern'), ('Europe/Zurich', 'Europe/Zurich'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Indian/Reunion', 'Indian/Reunion'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Juneau', 'America/Juneau'), ('Australia/Hobart', 'Australia/Hobart'), ('US/Pacific', 'US/Pacific'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('America/Mexico_City', 'America/Mexico_City'), ('Indian/Chagos', 'Indian/Chagos'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Europe/Vienna', 'Europe/Vienna'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Europe/Sofia', 'Europe/Sofia'), ('CST6CDT', 'CST6CDT'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Edmonton', 'America/Edmonton'), ('Indian/Cocos', 'Indian/Cocos'), ('Brazil/Acre', 'Brazil/Acre'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('US/Aleutian', 'US/Aleutian'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Portugal', 'Portugal'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Africa/Juba', 'Africa/Juba'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Australia/Queensland', 'Australia/Queensland'), ('Israel', 'Israel'), ('America/Caracas', 'America/Caracas'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Virgin', 'America/Virgin'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Grenada', 'America/Grenada'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Hongkong', 'Hongkong'), ('Etc/UCT', 'Etc/UCT'), ('Cuba', 'Cuba'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Asia/Vientiane', 'Asia/Vientiane'), ('America/Guatemala', 'America/Guatemala'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Australia/Sydney', 'Australia/Sydney'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/Belize', 'America/Belize'), ('Chile/Continental', 'Chile/Continental'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Halifax', 'America/Halifax'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Asia/Beirut', 'Asia/Beirut'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Swift_Current', 'America/Swift_Current'), ('Canada/Mountain', 'Canada/Mountain'), ('EST5EDT', 'EST5EDT'), ('Europe/Tallinn', 'Europe/Tallinn'), ('US/Mountain', 'US/Mountain'), ('Asia/Hovd', 'Asia/Hovd'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('UTC', 'UTC'), ('America/New_York', 'America/New_York'), ('Australia/ACT', 'Australia/ACT'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Antigua', 'America/Antigua'), ('GB', 'GB'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Europe/Budapest', 'Europe/Budapest'), ('Asia/Dili', 'Asia/Dili'), ('Asia/Samarkand', 'Asia/Samarkand'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Guayaquil', 'America/Guayaquil'), ('Australia/Adelaide', 'Australia/Adelaide'), ('US/East-Indiana', 'US/East-Indiana'), ('Europe/Skopje', 'Europe/Skopje'), ('Australia/LHI', 'Australia/LHI'), ('America/Santarem', 'America/Santarem'), ('Africa/Accra', 'Africa/Accra'), ('EET', 'EET'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Montevideo', 'America/Montevideo'), ('Etc/GMT-12', 'Etc/GMT-12'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('America/Denver', 'America/Denver'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Africa/Dakar', 'Africa/Dakar'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('US/Central', 'US/Central'), ('Brazil/East', 'Brazil/East'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('US/Arizona', 'US/Arizona'), ('America/Martinique', 'America/Martinique'), ('America/Dawson', 'America/Dawson'), ('Europe/Riga', 'Europe/Riga'), ('America/Metlakatla', 'America/Metlakatla'), ('MST7MDT', 'MST7MDT'), ('America/Kralendijk', 'America/Kralendijk'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Iran', 'Iran'), ('Europe/Malta', 'Europe/Malta'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Etc/GMT', 'Etc/GMT'), ('Europe/Paris', 'Europe/Paris'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Australia/South', 'Australia/South'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Manaus', 'America/Manaus'), ('America/Belem', 'America/Belem'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/Whitehorse', 'America/Whitehorse'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Creston', 'America/Creston'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Nome', 'America/Nome'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Africa/Douala', 'Africa/Douala'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Greenwich', 'Greenwich'), ('W-SU', 'W-SU'), ('America/Nassau', 'America/Nassau'), ('America/Nipigon', 'America/Nipigon'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Anguilla', 'America/Anguilla'), ('Turkey', 'Turkey'), ('Asia/Seoul', 'Asia/Seoul'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Pacific/Guam', 'Pacific/Guam'), ('Asia/Taipei', 'Asia/Taipei'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Chita', 'Asia/Chita'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Egypt', 'Egypt'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Hermosillo', 'America/Hermosillo'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Atka', 'America/Atka'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Barbados', 'America/Barbados'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Europe/Kiev', 'Europe/Kiev'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Havana', 'America/Havana'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('GB-Eire', 'GB-Eire'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Toronto', 'America/Toronto'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('America/St_Thomas', 'America/St_Thomas'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('WET', 'WET'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('GMT-0', 'GMT-0'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Chicago', 'America/Chicago'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Australia/North', 'Australia/North'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Vatican', 'Europe/Vatican'), ('PST8PDT', 'PST8PDT'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Asia/Karachi', 'Asia/Karachi'), ('Africa/Tunis', 'Africa/Tunis'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Adak', 'America/Adak'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Navajo', 'Navajo'), ('Africa/Libreville', 'Africa/Libreville'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Asia/Harbin', 'Asia/Harbin'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Boise', 'America/Boise'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Indian/Maldives', 'Indian/Maldives'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Pacific/Easter', 'Pacific/Easter'), (
                'Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Regina', 'America/Regina'), ('America/Montserrat', 'America/Montserrat'), ('Australia/West', 'Australia/West'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Iceland', 'Iceland'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Europe/Monaco', 'Europe/Monaco'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Europe/Oslo', 'Europe/Oslo'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Tortola', 'America/Tortola'), ('Australia/Eucla', 'Australia/Eucla'), ('Factory', 'Factory'), ('Eire', 'Eire'), ('Asia/Tehran', 'Asia/Tehran'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('America/Bogota', 'America/Bogota'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Africa/Abidjan', 'Africa/Abidjan'), ('ROK', 'ROK'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Indian/Mahe', 'Indian/Mahe'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/Cayman', 'America/Cayman'), ('America/Cuiaba', 'America/Cuiaba'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/Aruba', 'America/Aruba'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Asia/Brunei', 'Asia/Brunei'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Singapore', 'Singapore'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Noronha', 'America/Noronha'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Yangon', 'Asia/Yangon'), ('America/Nuuk', 'America/Nuuk'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Vancouver', 'America/Vancouver'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Scoresbysund', 'America/Scoresbysund'), ('US/Alaska', 'US/Alaska'), ('Europe/Tirane', 'Europe/Tirane'), ('Pacific/Niue', 'Pacific/Niue'), ('Etc/GMT-14', 'Etc/GMT-14'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Europe/Saratov', 'Europe/Saratov'), ('America/Maceio', 'America/Maceio'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Africa/Bamako', 'Africa/Bamako'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Muscat', 'Asia/Muscat'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Asia/Hebron', 'Asia/Hebron'), ('America/Dominica', 'America/Dominica'), ('Africa/Kampala', 'Africa/Kampala'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Thule', 'America/Thule'), ('Asia/Aqtau', 'Asia/Aqtau'), ('America/St_Johns', 'America/St_Johns'), ('America/St_Vincent', 'America/St_Vincent'), ('MET', 'MET'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Cayenne', 'America/Cayenne'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Asia/Tomsk', 'Asia/Tomsk'), ('US/Michigan', 'US/Michigan'), ('Asia/Amman', 'Asia/Amman'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Africa/Harare', 'Africa/Harare'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Canada/Central', 'Canada/Central'), ('Africa/Luanda', 'Africa/Luanda'), ('GMT+0', 'GMT+0'), ('Etc/GMT0', 'Etc/GMT0'), ('UCT', 'UCT'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Etc/UTC', 'Etc/UTC'), ('MST', 'MST'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Sitka', 'America/Sitka'), ('Africa/Malabo', 'Africa/Malabo'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Libya', 'Libya'), ('America/Monterrey', 'America/Monterrey'), ('Europe/Athens', 'Europe/Athens'), ('HST', 'HST'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Kuching', 'Asia/Kuching'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('America/St_Lucia', 'America/St_Lucia'), ('Pacific/Efate', 'Pacific/Efate'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Jujuy', 'America/Jujuy'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Ensenada', 'America/Ensenada'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('America/Mendoza', 'America/Mendoza'), ('America/Chihuahua', 'America/Chihuahua'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Europe/Berlin', 'Europe/Berlin'), ('Asia/Baku', 'Asia/Baku'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Africa/Maseru', 'Africa/Maseru'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Etc/GMT-0', 'Etc/GMT-0'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Asia/Macao', 'Asia/Macao'), ('Japan', 'Japan'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Marigot', 'America/Marigot'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Africa/Bissau', 'Africa/Bissau'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Yakutat', 'America/Yakutat'), ('America/Jamaica', 'America/Jamaica'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Europe/Andorra', 'Europe/Andorra'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('America/Cordoba', 'America/Cordoba'), ('Pacific/Apia', 'Pacific/Apia'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Etc/Zulu', 'Etc/Zulu'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Zulu', 'Zulu'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Atikokan', 'America/Atikokan'), ('Europe/Prague', 'Europe/Prague'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Universal', 'Universal'), ('Mexico/General', 'Mexico/General'), ('Asia/Nicosia', 'Asia/Nicosia'), ('America/Shiprock', 'America/Shiprock'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Managua', 'America/Managua'), ('Asia/Colombo', 'Asia/Colombo'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Godthab', 'America/Godthab'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Asia/Oral', 'Asia/Oral'), ('America/Rosario', 'America/Rosario'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/Guyana', 'America/Guyana'), ('Australia/Perth', 'Australia/Perth'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Europe/Rome', 'Europe/Rome'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Curacao', 'America/Curacao'), ('Africa/Kigali', 'Africa/Kigali'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Lima', 'America/Lima'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Africa/Cairo', 'Africa/Cairo'), ('Europe/Samara', 'Europe/Samara'), ('Brazil/West', 'Brazil/West'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Europe/Busingen', 'Europe/Busingen'), ('US/Hawaii', 'US/Hawaii'), ('America/La_Paz', 'America/La_Paz'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Europe/Minsk', 'Europe/Minsk'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Mazatlan', 'America/Mazatlan'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Freetown', 'Africa/Freetown'), ('EST', 'EST'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Asia/Macau', 'Asia/Macau'), ('Asia/Aden', 'Asia/Aden'), ('Europe/Madrid', 'Europe/Madrid'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Europe/Guernsey', 'Europe/Guernsey'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Phoenix', 'America/Phoenix'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Recife', 'America/Recife'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Africa/Lagos', 'Africa/Lagos'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('GMT', 'GMT'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Australia/Currie', 'Australia/Currie'), ('America/Asuncion', 'America/Asuncion'), ('US/Samoa', 'US/Samoa'), ('Poland', 'Poland'), ('Asia/Omsk', 'Asia/Omsk'), ('Africa/Niamey', 'Africa/Niamey'), ('America/Resolute', 'America/Resolute'), ('Asia/Manila', 'Asia/Manila'), ('America/St_Kitts', 'America/St_Kitts'), ('Australia/Victoria', 'Australia/Victoria'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Anchorage', 'America/Anchorage'), ('America/Araguaina', 'America/Araguaina'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Africa/Lome', 'Africa/Lome'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Australia/Darwin', 'Australia/Darwin'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/Santiago', 'America/Santiago'), ('Etc/GMT-8', 'Etc/GMT-8'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('America/Panama', 'America/Panama'), ('America/Menominee', 'America/Menominee'), ('NZ', 'NZ'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Canada/Eastern', 'Canada/Eastern'), ('Africa/Asmara', 'Africa/Asmara'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Africa/Maputo', 'Africa/Maputo'), ('Europe/London', 'Europe/London'), ('GMT0', 'GMT0'), ('ROC', 'ROC'), ('America/Louisville', 'America/Louisville'), ('America/Tijuana', 'America/Tijuana'), ('Jamaica', 'Jamaica'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Matamoros', 'America/Matamoros')], default='Europe/London', max_length=35),
        ),
    ]
