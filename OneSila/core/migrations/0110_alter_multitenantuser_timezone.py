# Generated by Django 5.0.2 on 2024-07-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0109_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Etc/GMT+3', 'Etc/GMT+3'), ('America/Atikokan', 'America/Atikokan'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Whitehorse', 'America/Whitehorse'), ('Africa/Luanda', 'Africa/Luanda'), ('W-SU', 'W-SU'), ('Asia/Damascus', 'Asia/Damascus'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Australia/Perth', 'Australia/Perth'), ('Europe/Riga', 'Europe/Riga'), ('America/Metlakatla', 'America/Metlakatla'), ('America/St_Kitts', 'America/St_Kitts'), ('PST8PDT', 'PST8PDT'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('US/Central', 'US/Central'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Grenada', 'America/Grenada'), ('America/Tortola', 'America/Tortola'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Martinique', 'America/Martinique'), ('America/Virgin', 'America/Virgin'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Jujuy', 'America/Jujuy'), ('Africa/Harare', 'Africa/Harare'), ('US/Aleutian', 'US/Aleutian'), ('Europe/Sofia', 'Europe/Sofia'), ('GMT+0', 'GMT+0'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Africa/Freetown', 'Africa/Freetown'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Europe/Madrid', 'Europe/Madrid'), ('Indian/Christmas', 'Indian/Christmas'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Barbados', 'America/Barbados'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Jamaica', 'America/Jamaica'), ('Asia/Hebron', 'Asia/Hebron'), ('Africa/Asmera', 'Africa/Asmera'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Edmonton', 'America/Edmonton'), ('Africa/Algiers', 'Africa/Algiers'), ('Europe/Kirov', 'Europe/Kirov'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/St_Lucia', 'America/St_Lucia'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Creston', 'America/Creston'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Phoenix', 'America/Phoenix'), ('Kwajalein', 'Kwajalein'), ('America/Havana', 'America/Havana'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Pacific/Guam', 'Pacific/Guam'), ('Asia/Makassar', 'Asia/Makassar'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Asia/Oral', 'Asia/Oral'), ('Etc/GMT+4', 'Etc/GMT+4'), ('GB', 'GB'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Europe/Berlin', 'Europe/Berlin'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Amman', 'Asia/Amman'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Marigot', 'America/Marigot'), ('Libya', 'Libya'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Mexico_City', 'America/Mexico_City'), ('Europe/Paris', 'Europe/Paris'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Asia/Harbin', 'Asia/Harbin'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Canada/Yukon', 'Canada/Yukon'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Montserrat', 'America/Montserrat'), ('Etc/GMT+8', 'Etc/GMT+8'), ('MST', 'MST'), ('America/Merida', 'America/Merida'), ('America/Eirunepe', 'America/Eirunepe'), ('Asia/Aden', 'Asia/Aden'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Noronha', 'America/Noronha'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Bahia', 'America/Bahia'), ('America/Aruba', 'America/Aruba'), ('Etc/GMT', 'Etc/GMT'), ('America/Dawson', 'America/Dawson'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('US/Hawaii', 'US/Hawaii'), ('America/Adak', 'America/Adak'), ('Etc/GMT0', 'Etc/GMT0'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Australia/ACT', 'Australia/ACT'), ('Africa/Lagos', 'Africa/Lagos'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('America/Mazatlan', 'America/Mazatlan'), ('Zulu', 'Zulu'), ('America/Denver', 'America/Denver'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Montreal', 'America/Montreal'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Atka', 'America/Atka'), ('America/Ensenada', 'America/Ensenada'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Turkey', 'Turkey'), ('Africa/Bamako', 'Africa/Bamako'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Indianapolis', 'America/Indianapolis'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Saigon', 'Asia/Saigon'), ('Asia/Qatar', 'Asia/Qatar'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Africa/Bangui', 'Africa/Bangui'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Halifax', 'America/Halifax'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Africa/Maseru', 'Africa/Maseru'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Indian/Reunion', 'Indian/Reunion'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Asia/Gaza', 'Asia/Gaza'), ('ROC', 'ROC'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('America/St_Vincent', 'America/St_Vincent'), ('America/Guyana', 'America/Guyana'), ('US/Alaska', 'US/Alaska'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Maceio', 'America/Maceio'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Nuuk', 'America/Nuuk'), ('America/Ojinaga', 'America/Ojinaga'), ('Australia/Queensland', 'Australia/Queensland'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Catamarca', 'America/Catamarca'), ('CST6CDT', 'CST6CDT'), ('America/Antigua', 'America/Antigua'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Europe/Busingen', 'Europe/Busingen'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Seoul', 'Asia/Seoul'), ('Greenwich', 'Greenwich'), ('America/Cuiaba', 'America/Cuiaba'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Africa/Juba', 'Africa/Juba'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Africa/Malabo', 'Africa/Malabo'), ('Europe/Athens', 'Europe/Athens'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/Yakutat', 'America/Yakutat'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Japan', 'Japan'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Australia/LHI', 'Australia/LHI'), ('US/Samoa', 'US/Samoa'), ('Pacific/Chatham', 'Pacific/Chatham'), ('US/Mountain', 'US/Mountain'), ('Europe/Jersey', 'Europe/Jersey'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Dili', 'Asia/Dili'), ('America/Montevideo', 'America/Montevideo'), ('Australia/South', 'Australia/South'), ('Africa/Monrovia', 'Africa/Monrovia'), ('CET', 'CET'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Cuba', 'Cuba'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Swift_Current', 'America/Swift_Current'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('PRC', 'PRC'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Europe/Samara', 'Europe/Samara'), ('America/Guatemala', 'America/Guatemala'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Sitka', 'America/Sitka'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Mexico/General', 'Mexico/General'), ('America/Thule', 'America/Thule'), ('NZ', 'NZ'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Chicago', 'America/Chicago'), ('Asia/Yangon', 'Asia/Yangon'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Africa/Bissau', 'Africa/Bissau'), ('Europe/Prague', 'Europe/Prague'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Australia/West', 'Australia/West'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Santiago', 'America/Santiago'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Universal', 'Universal'), ('Asia/Muscat', 'Asia/Muscat'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('America/Belem', 'America/Belem'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Resolute', 'America/Resolute'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Hongkong', 'Hongkong'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Monterrey', 'America/Monterrey'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Manila', 'Asia/Manila'), ('GMT0', 'GMT0'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Africa/Asmara', 'Africa/Asmara'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('UTC', 'UTC'), ('America/New_York', 'America/New_York'), ('America/Asuncion', 'America/Asuncion'), ('Asia/Baku', 'Asia/Baku'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Juneau', 'America/Juneau'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Africa/Kigali', 'Africa/Kigali'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Australia/NSW', 'Australia/NSW'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('America/Vancouver', 'America/Vancouver'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Kashgar', 'Asia/Kashgar'), ('WET', 'WET'), ('Asia/Dacca', 'Asia/Dacca'), ('Europe/Rome', 'Europe/Rome'), ('America/Recife', 'America/Recife'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Pacific/Pago_Pago',
                                   'Pacific/Pago_Pago'), ('Australia/Sydney', 'Australia/Sydney'), ('Africa/Libreville', 'Africa/Libreville'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Caracas', 'America/Caracas'), ('Egypt', 'Egypt'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Etc/GMT-12', 'Etc/GMT-12'), ('America/Managua', 'America/Managua'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Europe/Minsk', 'Europe/Minsk'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Guayaquil', 'America/Guayaquil'), ('Israel', 'Israel'), ('Europe/Chisinau', 'Europe/Chisinau'), ('US/Eastern', 'US/Eastern'), ('Indian/Maldives', 'Indian/Maldives'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Knox_IN', 'America/Knox_IN'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Dominica', 'America/Dominica'), ('America/Nome', 'America/Nome'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Africa/Blantyre', 'Africa/Blantyre'), ('America/Godthab', 'America/Godthab'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Manaus', 'America/Manaus'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Africa/Lome', 'Africa/Lome'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Moncton', 'America/Moncton'), ('Europe/Saratov', 'Europe/Saratov'), ('America/Iqaluit', 'America/Iqaluit'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Europe/Monaco', 'Europe/Monaco'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Indian/Chagos', 'Indian/Chagos'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/St_Thomas', 'America/St_Thomas'), ('Australia/Victoria', 'Australia/Victoria'), ('GB-Eire', 'GB-Eire'), ('America/Menominee', 'America/Menominee'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Singapore', 'Singapore'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Australia/Darwin', 'Australia/Darwin'), ('Asia/Macau', 'Asia/Macau'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Europe/Dublin', 'Europe/Dublin'), ('UCT', 'UCT'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Nipigon', 'America/Nipigon'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Fortaleza', 'America/Fortaleza'), ('Navajo', 'Navajo'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('EST5EDT', 'EST5EDT'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Africa/Accra', 'Africa/Accra'), ('Europe/London', 'Europe/London'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Pacific/Truk', 'Pacific/Truk'), ('Poland', 'Poland'), ('America/Regina', 'America/Regina'), ('America/St_Johns', 'America/St_Johns'), ('Asia/Almaty', 'Asia/Almaty'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('MST7MDT', 'MST7MDT'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Europe/Vatican', 'Europe/Vatican'), ('EST', 'EST'), ('Canada/Pacific', 'Canada/Pacific'), ('Etc/Universal', 'Etc/Universal'), ('America/Boa_Vista', 'America/Boa_Vista'), ('NZ-CHAT', 'NZ-CHAT'), ('Asia/Brunei', 'Asia/Brunei'), ('America/Paramaribo', 'America/Paramaribo'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('America/Boise', 'America/Boise'), ('America/Nassau', 'America/Nassau'), ('Pacific/Yap', 'Pacific/Yap'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Australia/Hobart', 'Australia/Hobart'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Anguilla', 'America/Anguilla'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Asia/Colombo', 'Asia/Colombo'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Winnipeg', 'America/Winnipeg'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Singapore', 'Asia/Singapore'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Asia/Chungking', 'Asia/Chungking'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Brazil/West', 'Brazil/West'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Asia/Magadan', 'Asia/Magadan'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Iceland', 'Iceland'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Shiprock', 'America/Shiprock'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Panama', 'America/Panama'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Factory', 'Factory'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Eire', 'Eire'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Lima', 'America/Lima'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/Tijuana', 'America/Tijuana'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('America/Louisville', 'America/Louisville'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Etc/UTC', 'Etc/UTC'), ('Africa/Kampala', 'Africa/Kampala'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('US/Michigan', 'US/Michigan'), ('Indian/Mahe', 'Indian/Mahe'), ('Africa/Douala', 'Africa/Douala'), ('America/Rosario', 'America/Rosario'), ('Chile/Continental', 'Chile/Continental'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Araguaina', 'America/Araguaina'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Europe/Vienna', 'Europe/Vienna'), ('Asia/Kuwait', 'Asia/Kuwait'), ('EET', 'EET'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Cancun', 'America/Cancun'), ('America/Mendoza', 'America/Mendoza'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Detroit', 'America/Detroit'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Miquelon', 'America/Miquelon'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Anchorage', 'America/Anchorage'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Etc/Zulu', 'Etc/Zulu'), ('Australia/North', 'Australia/North'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/Curacao', 'America/Curacao'), ('Europe/Volgograd', 'Europe/Volgograd'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Toronto', 'America/Toronto'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Canada/Central', 'Canada/Central'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Iran', 'Iran'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('US/Arizona', 'US/Arizona'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Africa/Cairo', 'Africa/Cairo'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Africa/Tunis', 'Africa/Tunis'), ('America/Cayman', 'America/Cayman'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Belize', 'America/Belize'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Atlantic/Azores', 'Atlantic/Azores'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Kolkata', 'Asia/Kolkata'), ('HST', 'HST'), ('Pacific/Wake', 'Pacific/Wake'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Inuvik', 'America/Inuvik'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Los_Angeles', 'America/Los_Angeles'), ('MET', 'MET'), ('US/Pacific', 'US/Pacific'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Asia/Omsk', 'Asia/Omsk'), ('Europe/Brussels', 'Europe/Brussels'), ('GMT', 'GMT'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Matamoros', 'America/Matamoros'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Asia/Kuching', 'Asia/Kuching'), ('America/El_Salvador', 'America/El_Salvador'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Beirut', 'Asia/Beirut'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Portugal', 'Portugal'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/Bogota', 'America/Bogota'), ('America/La_Paz', 'America/La_Paz'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Europe/Tirane', 'Europe/Tirane'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Pacific/Easter', 'Pacific/Easter'), ('Etc/UCT', 'Etc/UCT'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Asia/Dubai', 'Asia/Dubai'), ('Asia/Macao', 'Asia/Macao'), ('Europe/Malta', 'Europe/Malta'), ('America/Kralendijk', 'America/Kralendijk'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Santarem', 'America/Santarem'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Jamaica', 'Jamaica'), ('Pacific/Palau', 'Pacific/Palau'), ('Asia/Taipei', 'Asia/Taipei'), ('Brazil/Acre', 'Brazil/Acre'), ('ROK', 'ROK'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Brazil/East', 'Brazil/East'), ('Asia/Chita', 'Asia/Chita'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Cayenne', 'America/Cayenne'), ('build/etc/localtime', 'build/etc/localtime'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('GMT-0', 'GMT-0'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Europe/Zurich', 'Europe/Zurich'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Tehran', 'Asia/Tehran'), ('Etc/GMT-14', 'Etc/GMT-14')], default='Europe/London', max_length=35),
        ),
    ]
