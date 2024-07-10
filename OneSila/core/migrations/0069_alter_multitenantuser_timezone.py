# Generated by Django 5.0.2 on 2024-05-30 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('America/Belize', 'America/Belize'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Resolute', 'America/Resolute'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Pacific/Wake', 'Pacific/Wake'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Africa/Tripoli', 'Africa/Tripoli'), ('US/Pacific', 'US/Pacific'), ('America/Yakutat', 'America/Yakutat'), ('America/Goose_Bay', 'America/Goose_Bay'), ('MST7MDT', 'MST7MDT'), ('America/New_York', 'America/New_York'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Australia/ACT', 'Australia/ACT'), ('America/Mazatlan', 'America/Mazatlan'), ('Etc/UCT', 'Etc/UCT'), ('Poland', 'Poland'), ('Etc/GMT-6', 'Etc/GMT-6'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('build/etc/localtime', 'build/etc/localtime'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Atikokan', 'America/Atikokan'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/La_Paz', 'America/La_Paz'), ('Etc/GMT', 'Etc/GMT'), ('Asia/Chita', 'Asia/Chita'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Pacific/Midway', 'Pacific/Midway'), ('America/Recife', 'America/Recife'), ('America/Cayman', 'America/Cayman'), ('Europe/Andorra', 'Europe/Andorra'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Africa/Asmera', 'Africa/Asmera'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Indianapolis', 'America/Indianapolis'), ('Etc/Zulu', 'Etc/Zulu'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Managua', 'America/Managua'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Europe/Tirane', 'Europe/Tirane'), ('US/Mountain', 'US/Mountain'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Asia/Pontianak', 'Asia/Pontianak'), ('America/Yellowknife', 'America/Yellowknife'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Montreal', 'America/Montreal'), ('Africa/Cairo', 'Africa/Cairo'), ('Eire', 'Eire'), ('Asia/Damascus', 'Asia/Damascus'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Asia/Kuching', 'Asia/Kuching'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Iceland', 'Iceland'), ('America/Cordoba', 'America/Cordoba'), ('America/Chicago', 'America/Chicago'), ('America/Rosario', 'America/Rosario'), ('Europe/Vienna', 'Europe/Vienna'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Europe/Riga', 'Europe/Riga'), ('EET', 'EET'), ('Indian/Comoro', 'Indian/Comoro'), ('Pacific/Niue', 'Pacific/Niue'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Pacific/Truk', 'Pacific/Truk'), ('Pacific/Easter', 'Pacific/Easter'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('US/Samoa', 'US/Samoa'), ('Turkey', 'Turkey'), ('Etc/GMT-7', 'Etc/GMT-7'), ('US/Hawaii', 'US/Hawaii'), ('US/Alaska', 'US/Alaska'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Merida', 'America/Merida'), ('Asia/Karachi', 'Asia/Karachi'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('UCT', 'UCT'), ('US/Michigan', 'US/Michigan'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Atka', 'America/Atka'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Taipei', 'Asia/Taipei'), ('GB-Eire', 'GB-Eire'), ('Europe/Rome', 'Europe/Rome'), ('America/Montserrat', 'America/Montserrat'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('US/Eastern', 'US/Eastern'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('US/Aleutian', 'US/Aleutian'), ('Europe/Dublin', 'Europe/Dublin'), ('Europe/Prague', 'Europe/Prague'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Panama', 'America/Panama'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Mexico_City', 'America/Mexico_City'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Denver', 'America/Denver'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Europe/Skopje', 'Europe/Skopje'), ('Africa/Lagos', 'Africa/Lagos'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Barbados', 'America/Barbados'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/Anguilla', 'America/Anguilla'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Jamaica', 'Jamaica'), ('Africa/Douala', 'Africa/Douala'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Aruba', 'America/Aruba'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Anchorage', 'America/Anchorage'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Europe/Athens', 'Europe/Athens'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Pacific/Apia', 'Pacific/Apia'), ('Asia/Tehran', 'Asia/Tehran'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Boise', 'America/Boise'), ('PRC', 'PRC'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Pacific/Guam', 'Pacific/Guam'), ('Africa/Harare', 'Africa/Harare'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Whitehorse', 'America/Whitehorse'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Tijuana', 'America/Tijuana'), ('Europe/Malta', 'Europe/Malta'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Halifax', 'America/Halifax'), ('Asia/Makassar', 'Asia/Makassar'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Bahia', 'America/Bahia'), ('America/Inuvik', 'America/Inuvik'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Australia/Darwin', 'Australia/Darwin'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('America/Curacao', 'America/Curacao'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Asia/Baku', 'Asia/Baku'), ('GMT0', 'GMT0'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Europe/Saratov', 'Europe/Saratov'), ('Africa/Kigali', 'Africa/Kigali'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Indian/Maldives', 'Indian/Maldives'), ('Israel', 'Israel'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Asia/Kabul', 'Asia/Kabul'), ('Europe/Madrid', 'Europe/Madrid'), ('America/Juneau', 'America/Juneau'), ('Canada/Yukon', 'Canada/Yukon'), ('Canada/Mountain', 'Canada/Mountain'), ('Navajo', 'Navajo'), ('America/Catamarca', 'America/Catamarca'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Indian/Reunion', 'Indian/Reunion'), ('Europe/London', 'Europe/London'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Europe/Belfast', 'Europe/Belfast'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Maceio', 'America/Maceio'), ('America/Hermosillo', 'America/Hermosillo'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/Caracas', 'America/Caracas'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Australia/LHI', 'Australia/LHI'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Los_Angeles', 'America/Los_Angeles'), ('America/Tortola', 'America/Tortola'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Australia/Perth', 'Australia/Perth'), ('America/Martinique', 'America/Martinique'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Menominee', 'America/Menominee'), ('Africa/Maputo', 'Africa/Maputo'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Guyana', 'America/Guyana'), ('Factory', 'Factory'), ('Asia/Manila', 'Asia/Manila'), ('PST8PDT', 'PST8PDT'), ('GB', 'GB'), ('NZ-CHAT', 'NZ-CHAT'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Havana', 'America/Havana'), ('Africa/Niamey', 'Africa/Niamey'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Almaty', 'Asia/Almaty'), ('Universal', 'Universal'), ('GMT+0', 'GMT+0'), ('America/Grenada', 'America/Grenada'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Asia/Amman', 'Asia/Amman'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Magadan', 'Asia/Magadan'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Iran', 'Iran'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Moncton', 'America/Moncton'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/Manaus', 'America/Manaus'), ('Greenwich', 'Greenwich'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Montevideo', 'America/Montevideo'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Zulu', 'Zulu'), ('America/Ojinaga', 'America/Ojinaga'), ('Australia/Sydney', 'Australia/Sydney'), ('Etc/GMT+3', 'Etc/GMT+3'), ('America/Santarem', 'America/Santarem'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Etc/UTC', 'Etc/UTC'), ('America/Monterrey', 'America/Monterrey'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Libya', 'Libya'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Australia/Canberra', 'Australia/Canberra'), ('Europe/Samara', 'Europe/Samara'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Ensenada', 'America/Ensenada'), ('Europe/Brussels', 'Europe/Brussels'), ('MET', 'MET'), ('W-SU', 'W-SU'), ('America/Creston', 'America/Creston'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Kralendijk', 'America/Kralendijk'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Europe/Oslo', 'Europe/Oslo'), ('GMT', 'GMT'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Europe/Sofia', 'Europe/Sofia'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Africa/Malabo', 'Africa/Malabo'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Portugal', 'Portugal'), ('America/St_Thomas', 'America/St_Thomas'), ('US/East-Indiana', 'US/East-Indiana'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Europe/Kiev', 'Europe/Kiev'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/St_Kitts', 'America/St_Kitts'), ('Indian/Mahe', 'Indian/Mahe'), ('America/Cuiaba', 'America/Cuiaba'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Europe/Jersey', 'Europe/Jersey'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Indian/Chagos', 'Indian/Chagos'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Noronha', 'America/Noronha'), ('Asia/Qatar', 'Asia/Qatar'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Chile/Continental', 'Chile/Continental'), ('ROC', 'ROC'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Australia/North', 'Australia/North'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('EST', 'EST'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Asia/Dili', 'Asia/Dili'), ('MST', 'MST'), ('America/Lima', 'America/Lima'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Fortaleza', 'America/Fortaleza'), ('Asia/Macao', 'Asia/Macao'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Africa/Tunis', 'Africa/Tunis'), ('America/St_Johns', 'America/St_Johns'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Africa/Freetown', 'Africa/Freetown'), ('Australia/West', 'Australia/West'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Vancouver', 'America/Vancouver'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Europe/San_Marino', 'Europe/San_Marino'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Belem', 'America/Belem'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Santiago', 'America/Santiago'), ('America/Swift_Current', 'America/Swift_Current'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('UTC', 'UTC'), ('America/Metlakatla', 'America/Metlakatla'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Harbin', 'Asia/Harbin'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Asia/Beirut', 'Asia/Beirut'), ('Europe/Budapest', 'Europe/Budapest'), ('NZ', 'NZ'), ('Asia/Tomsk', 'Asia/Tomsk'), ('America/Asuncion', 'America/Asuncion'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Thule', 'America/Thule'), ('Asia/Muscat', 'Asia/Muscat'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Louisville', 'America/Louisville'), ('Asia/Brunei', 'Asia/Brunei'), ('Asia/Hovd', 'Asia/Hovd'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Pacific/Wallis', 'Pacific/Wallis'), ('CET', 'CET'), ('Europe/Kirov', 'Europe/Kirov'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Eirunepe', 'America/Eirunepe'), ('Africa/Gaborone', 'Africa/Gaborone'), ('America/Nome', 'America/Nome'), ('America/Winnipeg', 'America/Winnipeg'), ('US/Central', 'US/Central'), ('Europe/Minsk', 'Europe/Minsk'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Australia/NSW', 'Australia/NSW'), ('US/Arizona', 'US/Arizona'), ('Europe/Paris', 'Europe/Paris'), ('Africa/Lome', 'Africa/Lome'), ('America/Cayenne', 'America/Cayenne'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Asia/Hebron', 'Asia/Hebron'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Etc/GMT0', 'Etc/GMT0'), ('Europe/Busingen', 'Europe/Busingen'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Asia/Gaza', 'Asia/Gaza'), ('HST', 'HST'), ('America/Edmonton', 'America/Edmonton'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Asia/Dubai', 'Asia/Dubai'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Australia/Queensland', 'Australia/Queensland'), ('GMT-0', 'GMT-0'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Europe/Monaco', 'Europe/Monaco'), ('America/El_Salvador', 'America/El_Salvador'), ('Europe/Moscow', 'Europe/Moscow'), ('Asia/Istanbul', 'Asia/Istanbul'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Mendoza', 'America/Mendoza'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Africa/Libreville', 'Africa/Libreville'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Europe/Berlin', 'Europe/Berlin'), ('Africa/Bamako', 'Africa/Bamako'), ('Asia/Colombo', 'Asia/Colombo'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Regina', 'America/Regina'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Bogota', 'America/Bogota'), ('America/Nipigon', 'America/Nipigon'), ('Pacific/Yap', 'Pacific/Yap'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Africa/Bangui', 'Africa/Bangui'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Asia/Omsk', 'Asia/Omsk'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/Adak', 'America/Adak'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Japan', 'Japan'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Hongkong', 'Hongkong'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Jayapura', 'Asia/Jayapura'), ('CST6CDT', 'CST6CDT'), ('America/Detroit', 'America/Detroit'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Australia/Hobart', 'Australia/Hobart'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Asia/Aden', 'Asia/Aden'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/Guatemala', 'America/Guatemala'), ('America/Sitka', 'America/Sitka'), ('America/Chihuahua', 'America/Chihuahua'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('America/Shiprock', 'America/Shiprock'), ('Brazil/Acre', 'Brazil/Acre'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Asia/Khandyga', 'Asia/Khandyga'), ('WET', 'WET'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Australia/Currie', 'Australia/Currie'), ('America/Marigot', 'America/Marigot'), ('America/Godthab', 'America/Godthab'), ('Africa/Accra', 'Africa/Accra'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Brazil/East', 'Brazil/East'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Asia/Yangon', 'Asia/Yangon'), ('Asia/Dacca', 'Asia/Dacca'), ('America/Virgin', 'America/Virgin'), ('Australia/South', 'Australia/South'), ('EST5EDT', 'EST5EDT'), ('America/Jujuy', 'America/Jujuy'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Dominica', 'America/Dominica'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/St_Vincent', 'America/St_Vincent'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Asia/Saigon', 'Asia/Saigon'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Africa/Juba', 'Africa/Juba'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Etc/Universal', 'Etc/Universal'), ('America/Nassau', 'America/Nassau'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Bishkek', 'Asia/Bishkek'), ('America/Araguaina', 'America/Araguaina'), ('America/Miquelon', 'America/Miquelon'), ('America/Nuuk', 'America/Nuuk'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Africa/Conakry', 'Africa/Conakry'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Jamaica', 'America/Jamaica'), ('Asia/Oral', 'Asia/Oral'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Brazil/West', 'Brazil/West'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Singapore', 'Singapore'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Canada/Central', 'Canada/Central'), ('Mexico/General', 'Mexico/General'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Africa/Kampala', 'Africa/Kampala'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Antigua', 'America/Antigua'), ('America/Matamoros', 'America/Matamoros'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Asia/Macau', 'Asia/Macau'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Africa/Asmara', 'Africa/Asmara'), ('America/Cancun', 'America/Cancun'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Cuba', 'Cuba'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Toronto', 'America/Toronto'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Kwajalein', 'Kwajalein'), ('Etc/GMT+5', 'Etc/GMT+5'), ('ROK', 'ROK'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Dawson', 'America/Dawson'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Phoenix', 'America/Phoenix'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Egypt', 'Egypt'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('America/St_Lucia', 'America/St_Lucia'), ('Australia/Victoria', 'Australia/Victoria'), ('Africa/Casablanca', 'Africa/Casablanca')], default='Europe/London', max_length=35),
        ),
    ]
