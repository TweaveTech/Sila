# Generated by Django 5.0.2 on 2024-04-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Africa/Bamako', 'Africa/Bamako'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Cancun', 'America/Cancun'), ('Asia/Baku', 'Asia/Baku'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Halifax', 'America/Halifax'), ('Singapore', 'Singapore'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/St_Vincent', 'America/St_Vincent'), ('America/Bahia', 'America/Bahia'), ('Egypt', 'Egypt'), ('W-SU', 'W-SU'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('ROK', 'ROK'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('US/Hawaii', 'US/Hawaii'), ('America/Eirunepe', 'America/Eirunepe'), ('Australia/Queensland', 'Australia/Queensland'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Kwajalein', 'Kwajalein'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Africa/Harare', 'Africa/Harare'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Universal', 'Universal'), ('America/Juneau', 'America/Juneau'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('America/Mazatlan', 'America/Mazatlan'), ('America/Caracas', 'America/Caracas'), ('US/Pacific', 'US/Pacific'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Guyana', 'America/Guyana'), ('America/La_Paz', 'America/La_Paz'), ('Europe/Sofia', 'Europe/Sofia'), ('Africa/Cairo', 'Africa/Cairo'), ('Europe/Paris', 'Europe/Paris'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Martinique', 'America/Martinique'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Montreal', 'America/Montreal'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Hongkong', 'Hongkong'), ('PRC', 'PRC'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Makassar', 'Asia/Makassar'), ('Etc/Zulu', 'Etc/Zulu'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Brazil/West', 'Brazil/West'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Dili', 'Asia/Dili'), ('Indian/Chagos', 'Indian/Chagos'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('America/Guatemala', 'America/Guatemala'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('HST', 'HST'), ('Etc/GMT-8', 'Etc/GMT-8'), ('EST', 'EST'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/El_Salvador', 'America/El_Salvador'), ('Europe/Belgrade', 'Europe/Belgrade'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Africa/Freetown', 'Africa/Freetown'), ('America/Knox_IN', 'America/Knox_IN'), ('Libya', 'Libya'), ('Asia/Muscat', 'Asia/Muscat'), ('America/Virgin', 'America/Virgin'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Brunei', 'Asia/Brunei'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Canada/Mountain', 'Canada/Mountain'), ('Australia/Hobart', 'Australia/Hobart'), ('Africa/Juba', 'Africa/Juba'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Asia/Singapore', 'Asia/Singapore'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Asia/Chita', 'Asia/Chita'), ('America/Anguilla', 'America/Anguilla'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Africa/Tunis', 'Africa/Tunis'), ('Asia/Oral', 'Asia/Oral'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Mendoza', 'America/Mendoza'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Australia/ACT', 'Australia/ACT'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Australia/NSW', 'Australia/NSW'), ('WET', 'WET'), ('Brazil/East', 'Brazil/East'), ('Asia/Colombo', 'Asia/Colombo'), ('CET', 'CET'), ('America/Inuvik', 'America/Inuvik'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/Goose_Bay', 'America/Goose_Bay'), ('GMT', 'GMT'), ('America/Yellowknife', 'America/Yellowknife'), ('Africa/Asmera', 'Africa/Asmera'), ('ROC', 'ROC'), ('America/Toronto', 'America/Toronto'), ('Europe/Monaco', 'Europe/Monaco'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Etc/UCT', 'Etc/UCT'), ('Europe/Zurich', 'Europe/Zurich'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Menominee', 'America/Menominee'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Jamaica', 'America/Jamaica'), ('US/Samoa', 'US/Samoa'), ('America/Louisville', 'America/Louisville'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Europe/Budapest', 'Europe/Budapest'), ('Africa/Malabo', 'Africa/Malabo'), ('America/Creston', 'America/Creston'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Navajo', 'Navajo'), ('US/Aleutian', 'US/Aleutian'), ('America/Nipigon', 'America/Nipigon'), ('America/Santarem', 'America/Santarem'), ('America/Adak', 'America/Adak'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Marigot', 'America/Marigot'), ('America/Managua', 'America/Managua'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Asia/Riyadh', 'Asia/Riyadh'), ('America/Resolute', 'America/Resolute'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Ensenada', 'America/Ensenada'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Cayman', 'America/Cayman'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Belem', 'America/Belem'), ('Europe/London', 'Europe/London'), ('America/Chihuahua', 'America/Chihuahua'), ('Asia/Magadan', 'Asia/Magadan'), ('Asia/Almaty', 'Asia/Almaty'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Africa/Libreville', 'Africa/Libreville'), ('Asia/Dacca', 'Asia/Dacca'), ('Europe/Andorra', 'Europe/Andorra'), ('Asia/Macau', 'Asia/Macau'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Asuncion', 'America/Asuncion'), ('GMT-0', 'GMT-0'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Tijuana', 'America/Tijuana'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('GB-Eire', 'GB-Eire'), ('Australia/Perth', 'Australia/Perth'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Araguaina', 'America/Araguaina'), ('America/Detroit', 'America/Detroit'), ('US/Eastern', 'US/Eastern'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Zulu', 'Zulu'), ('GMT+0', 'GMT+0'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Etc/GMT+7', 'Etc/GMT+7'), ('MST7MDT', 'MST7MDT'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Pacific/Palau', 'Pacific/Palau'), ('NZ', 'NZ'), ('Australia/Currie', 'Australia/Currie'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Africa/Niamey', 'Africa/Niamey'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Australia/Canberra', 'Australia/Canberra'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('America/Tortola', 'America/Tortola'), ('America/Antigua', 'America/Antigua'), ('Africa/Douala', 'Africa/Douala'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Taipei', 'Asia/Taipei'), ('Europe/Prague', 'Europe/Prague'), ('America/Barbados', 'America/Barbados'), ('Etc/GMT', 'Etc/GMT'), ('America/Paramaribo', 'America/Paramaribo'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Africa/Maseru', 'Africa/Maseru'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Hermosillo', 'America/Hermosillo'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('US/Central', 'US/Central'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Canada/Yukon', 'Canada/Yukon'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('America/Mexico_City', 'America/Mexico_City'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Curacao', 'America/Curacao'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Lima', 'America/Lima'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Aden', 'Asia/Aden'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Indian/Maldives', 'Indian/Maldives'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Indian/Mahe', 'Indian/Mahe'), ('Chile/Continental', 'Chile/Continental'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Etc/GMT-6', 'Etc/GMT-6'), ('America/Panama', 'America/Panama'), ('Asia/Harbin', 'Asia/Harbin'), ('America/New_York', 'America/New_York'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Europe/Vienna', 'Europe/Vienna'), ('Asia/Damascus', 'Asia/Damascus'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('America/Miquelon', 'America/Miquelon'), ('America/Regina', 'America/Regina'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Catamarca', 'America/Catamarca'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Lome', 'Africa/Lome'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Asia/Dubai', 'Asia/Dubai'), ('UTC', 'UTC'), ('Pacific/Niue', 'Pacific/Niue'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Atka', 'America/Atka'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Indian/Cocos', 'Indian/Cocos'), ('Etc/UTC', 'Etc/UTC'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Argentina/Rio_Gallegos',
                                   'America/Argentina/Rio_Gallegos'), ('Europe/Tirane', 'Europe/Tirane'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Nassau', 'America/Nassau'), ('America/Boise', 'America/Boise'), ('Europe/Madrid', 'Europe/Madrid'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Africa/Luanda', 'Africa/Luanda'), ('US/Arizona', 'US/Arizona'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Malta', 'Europe/Malta'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Europe/Riga', 'Europe/Riga'), ('America/Denver', 'America/Denver'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Santiago', 'America/Santiago'), ('Brazil/Acre', 'Brazil/Acre'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Asia/Kabul', 'Asia/Kabul'), ('Africa/Algiers', 'Africa/Algiers'), ('Israel', 'Israel'), ('Asia/Manila', 'Asia/Manila'), ('Europe/Kirov', 'Europe/Kirov'), ('Etc/GMT0', 'Etc/GMT0'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Monterrey', 'America/Monterrey'), ('Asia/Karachi', 'Asia/Karachi'), ('Africa/Kigali', 'Africa/Kigali'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Qatar', 'Asia/Qatar'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Atikokan', 'America/Atikokan'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Montevideo', 'America/Montevideo'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Anchorage', 'America/Anchorage'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Chicago', 'America/Chicago'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Europe/Jersey', 'Europe/Jersey'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Nome', 'America/Nome'), ('Asia/Kuwait', 'Asia/Kuwait'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Samarkand', 'Asia/Samarkand'), ('GMT0', 'GMT0'), ('America/Merida', 'America/Merida'), ('EET', 'EET'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Belize', 'America/Belize'), ('Europe/Minsk', 'Europe/Minsk'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Swift_Current', 'America/Swift_Current'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Greenwich', 'Greenwich'), ('Australia/Victoria', 'Australia/Victoria'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Canada/Central', 'Canada/Central'), ('US/Mountain', 'US/Mountain'), ('Factory', 'Factory'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Bogota', 'America/Bogota'), ('Pacific/Midway', 'Pacific/Midway'), ('US/Alaska', 'US/Alaska'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Asia/Hebron', 'Asia/Hebron'), ('PST8PDT', 'PST8PDT'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Recife', 'America/Recife'), ('America/St_Lucia', 'America/St_Lucia'), ('Asia/Omsk', 'Asia/Omsk'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Pacific/Yap', 'Pacific/Yap'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/Noronha', 'America/Noronha'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Manaus', 'America/Manaus'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Indian/Reunion', 'Indian/Reunion'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('US/Michigan', 'US/Michigan'), ('America/Maceio', 'America/Maceio'), ('MET', 'MET'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Cayenne', 'America/Cayenne'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Africa/Dakar', 'Africa/Dakar'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Asia/Yangon', 'Asia/Yangon'), ('America/Montserrat', 'America/Montserrat'), ('America/St_Thomas', 'America/St_Thomas'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Australia/South', 'Australia/South'), ('America/Thule', 'America/Thule'), ('Jamaica', 'Jamaica'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Europe/Samara', 'Europe/Samara'), ('Pacific/Truk', 'Pacific/Truk'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Turkey', 'Turkey'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Pontianak', 'Asia/Pontianak'), ('EST5EDT', 'EST5EDT'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Etc/Universal', 'Etc/Universal'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Pacific/Efate', 'Pacific/Efate'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Edmonton', 'America/Edmonton'), ('America/Vancouver', 'America/Vancouver'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Poland', 'Poland'), ('Europe/Brussels', 'Europe/Brussels'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Guayaquil', 'America/Guayaquil'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Havana', 'America/Havana'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Europe/Kiev', 'Europe/Kiev'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Canada/Eastern', 'Canada/Eastern'), ('Iran', 'Iran'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Iceland', 'Iceland'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Shiprock', 'America/Shiprock'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Mexico/General', 'Mexico/General'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('GB', 'GB'), ('America/Sitka', 'America/Sitka'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Rainy_River', 'America/Rainy_River'), ('Europe/Busingen', 'Europe/Busingen'), ('Europe/Moscow', 'Europe/Moscow'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Africa/Accra', 'Africa/Accra'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Asia/Macao', 'Asia/Macao'), ('America/Costa_Rica', 'America/Costa_Rica'), ('CST6CDT', 'CST6CDT'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Phoenix', 'America/Phoenix'), ('NZ-CHAT', 'NZ-CHAT'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Rosario', 'America/Rosario'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Europe/Rome', 'Europe/Rome'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Cuba', 'Cuba'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Cuiaba', 'America/Cuiaba'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/Indianapolis', 'America/Indianapolis'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Africa/Lagos', 'Africa/Lagos'), ('Europe/Berlin', 'Europe/Berlin'), ('Africa/Conakry', 'Africa/Conakry'), ('America/St_Johns', 'America/St_Johns'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Asia/Kuching', 'Asia/Kuching'), ('America/Dominica', 'America/Dominica'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Godthab', 'America/Godthab'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Australia/Eucla', 'Australia/Eucla'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Dawson', 'America/Dawson'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Africa/Banjul', 'Africa/Banjul'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Australia/North', 'Australia/North'), ('America/Nuuk', 'America/Nuuk'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Canada/Pacific', 'Canada/Pacific'), ('UCT', 'UCT'), ('US/East-Indiana', 'US/East-Indiana'), ('Europe/Belfast', 'Europe/Belfast'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('build/etc/localtime', 'build/etc/localtime'), ('Asia/Beirut', 'Asia/Beirut'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Eire', 'Eire'), ('Africa/Asmara', 'Africa/Asmara'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Grenada', 'America/Grenada'), ('Europe/Athens', 'Europe/Athens'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('MST', 'MST'), ('America/Moncton', 'America/Moncton'), ('America/Matamoros', 'America/Matamoros'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Australia/LHI', 'Australia/LHI'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Asia/Saigon', 'Asia/Saigon'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Africa/Kampala', 'Africa/Kampala'), ('America/Aruba', 'America/Aruba'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Portugal', 'Portugal'), ('Japan', 'Japan'), ('America/St_Kitts', 'America/St_Kitts'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Jujuy', 'America/Jujuy'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Pacific/Easter', 'Pacific/Easter'), ('Europe/Saratov', 'Europe/Saratov'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Australia/Darwin', 'Australia/Darwin'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Yakutat', 'America/Yakutat'), ('Australia/West', 'Australia/West'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Kralendijk', 'America/Kralendijk')], default='Europe/London', max_length=35),
        ),
    ]
