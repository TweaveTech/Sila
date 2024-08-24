# Generated by Django 5.0.2 on 2024-05-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Africa/Kampala', 'Africa/Kampala'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Paramaribo', 'America/Paramaribo'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Hebron', 'Asia/Hebron'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('MST', 'MST'), ('Africa/Tunis', 'Africa/Tunis'), ('Portugal', 'Portugal'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Navajo', 'Navajo'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Phoenix', 'America/Phoenix'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Caracas', 'America/Caracas'), ('America/Montreal', 'America/Montreal'), ('Japan', 'Japan'), ('America/Panama', 'America/Panama'), ('America/Araguaina', 'America/Araguaina'), ('Europe/Athens', 'Europe/Athens'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Africa/Kigali', 'Africa/Kigali'), ('Etc/Universal', 'Etc/Universal'), ('America/Jamaica', 'America/Jamaica'), ('Jamaica', 'Jamaica'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Nassau', 'America/Nassau'), ('Chile/Continental', 'Chile/Continental'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Africa/Douala', 'Africa/Douala'), ('Iran', 'Iran'), ('CST6CDT', 'CST6CDT'), ('America/Martinique', 'America/Martinique'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Europe/Rome', 'Europe/Rome'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('GB', 'GB'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Vienna', 'Europe/Vienna'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Asia/Damascus', 'Asia/Damascus'), ('Australia/Eucla', 'Australia/Eucla'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Atikokan', 'America/Atikokan'), ('America/Vancouver', 'America/Vancouver'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Virgin', 'America/Virgin'), ('Asia/Singapore', 'Asia/Singapore'), ('US/Pacific', 'US/Pacific'), ('America/Shiprock', 'America/Shiprock'), ('America/St_Vincent', 'America/St_Vincent'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Godthab', 'America/Godthab'), ('Etc/GMT-13', 'Etc/GMT-13'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Australia/NSW', 'Australia/NSW'), ('America/Asuncion', 'America/Asuncion'), ('Australia/LHI', 'Australia/LHI'), ('Asia/Qatar', 'Asia/Qatar'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Australia/South', 'Australia/South'), ('America/Mazatlan', 'America/Mazatlan'), ('Europe/Zurich', 'Europe/Zurich'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Nome', 'America/Nome'), ('America/Indianapolis', 'America/Indianapolis'), ('America/El_Salvador', 'America/El_Salvador'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Asia/Kuwait', 'Asia/Kuwait'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Africa/Lome', 'Africa/Lome'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Asia/Dacca', 'Asia/Dacca'), ('NZ', 'NZ'), ('Pacific/Guam', 'Pacific/Guam'), ('Asia/Oral', 'Asia/Oral'), ('UCT', 'UCT'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Barbados', 'America/Barbados'), ('Etc/GMT+6', 'Etc/GMT+6'), ('GB-Eire', 'GB-Eire'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Asia/Harbin', 'Asia/Harbin'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Thule', 'America/Thule'), ('Australia/Darwin', 'Australia/Darwin'), ('GMT+0', 'GMT+0'), ('America/Bahia', 'America/Bahia'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Africa/Bissau', 'Africa/Bissau'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Creston', 'America/Creston'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Tijuana', 'America/Tijuana'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Dawson', 'America/Dawson'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Africa/Maseru', 'Africa/Maseru'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Brazil/Acre', 'Brazil/Acre'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Asia/Baku', 'Asia/Baku'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Asia/Beirut', 'Asia/Beirut'), ('Australia/Victoria', 'Australia/Victoria'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Santiago', 'America/Santiago'), ('America/Regina', 'America/Regina'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Colombo', 'Asia/Colombo'), ('Pacific/Truk', 'Pacific/Truk'), ('Pacific/Palau', 'Pacific/Palau'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('build/etc/localtime', 'build/etc/localtime'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Asia/Aden', 'Asia/Aden'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Australia/Adelaide', 'Australia/Adelaide'), ('GMT', 'GMT'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Chungking', 'Asia/Chungking'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/Metlakatla', 'America/Metlakatla'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Etc/UTC', 'Etc/UTC'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Iqaluit', 'America/Iqaluit'), ('Europe/Monaco', 'Europe/Monaco'), ('Asia/Yerevan', 'Asia/Yerevan'), ('America/Noronha', 'America/Noronha'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Montserrat', 'America/Montserrat'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('America/Inuvik', 'America/Inuvik'), ('Cuba', 'Cuba'), ('Poland', 'Poland'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Belize', 'America/Belize'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Asia/Makassar', 'Asia/Makassar'), ('Pacific/Apia', 'Pacific/Apia'), ('America/St_Thomas', 'America/St_Thomas'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Havana', 'America/Havana'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Iceland', 'Iceland'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Canada/Eastern', 'Canada/Eastern'), ('Europe/Brussels', 'Europe/Brussels'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Mexico_City', 'America/Mexico_City'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Etc/GMT+4', 'Etc/GMT+4'), ('ROC', 'ROC'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/Ensenada', 'America/Ensenada'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Etc/GMT-10', 'Etc/GMT-10'), ('US/Hawaii', 'US/Hawaii'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Lima', 'America/Lima'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Magadan', 'Asia/Magadan'), ('Europe/London', 'Europe/London'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('America/Detroit', 'America/Detroit'), ('America/Boise', 'America/Boise'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Cancun', 'America/Cancun'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('US/Central', 'US/Central'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Europe/Samara', 'Europe/Samara'), ('Europe/Tirane', 'Europe/Tirane'), ('America/Bogota', 'America/Bogota'), ('US/Michigan', 'US/Michigan'), ('Kwajalein', 'Kwajalein'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Etc/UCT', 'Etc/UCT'), ('Africa/Dakar', 'Africa/Dakar'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Asia/Muscat', 'Asia/Muscat'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Africa/Harare', 'Africa/Harare'), ('America/Resolute', 'America/Resolute'), ('America/Tortola', 'America/Tortola'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Brazil/West', 'Brazil/West'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Africa/Asmera', 'Africa/Asmera'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Greenwich', 'Greenwich'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Europe/Oslo', 'Europe/Oslo'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('GMT0', 'GMT0'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Asia/Almaty', 'Asia/Almaty'), ('Asia/Chita', 'Asia/Chita'), ('America/Yellowknife', 'America/Yellowknife'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('ROK', 'ROK'), ('Hongkong', 'Hongkong'), ('America/Cayenne', 'America/Cayenne'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Canada/Pacific', 'Canada/Pacific'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Managua', 'America/Managua'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Africa/Maputo', 'Africa/Maputo'), ('America/La_Paz', 'America/La_Paz'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Pacific/Kanton', 'Pacific/Kanton'), ('US/Aleutian', 'US/Aleutian'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Montevideo', 'America/Montevideo'), ('America/Whitehorse', 'America/Whitehorse'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Sitka', 'America/Sitka'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Factory', 'Factory'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Nuuk', 'America/Nuuk'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Rosario', 'America/Rosario'), ('Asia/Dushanbe', 'Asia/Dushanbe'),
                                   ('GMT-0', 'GMT-0'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Matamoros', 'America/Matamoros'), ('EST', 'EST'), ('Africa/Cairo', 'Africa/Cairo'), ('Africa/Luanda', 'Africa/Luanda'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Manaus', 'America/Manaus'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Anchorage', 'America/Anchorage'), ('Europe/Riga', 'Europe/Riga'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('US/Eastern', 'US/Eastern'), ('Etc/Zulu', 'Etc/Zulu'), ('Europe/Jersey', 'Europe/Jersey'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Cuiaba', 'America/Cuiaba'), ('W-SU', 'W-SU'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Turkey', 'Turkey'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Belem', 'America/Belem'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Edmonton', 'America/Edmonton'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Canada/Mountain', 'Canada/Mountain'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Juneau', 'America/Juneau'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Aruba', 'America/Aruba'), ('Etc/GMT-12', 'Etc/GMT-12'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Singapore', 'Singapore'), ('Indian/Cocos', 'Indian/Cocos'), ('Asia/Riyadh', 'Asia/Riyadh'), ('US/Mountain', 'US/Mountain'), ('America/Monterrey', 'America/Monterrey'), ('America/Recife', 'America/Recife'), ('EST5EDT', 'EST5EDT'), ('America/Mendoza', 'America/Mendoza'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Asia/Macao', 'Asia/Macao'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Europe/Andorra', 'Europe/Andorra'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Libya', 'Libya'), ('PST8PDT', 'PST8PDT'), ('America/Anguilla', 'America/Anguilla'), ('America/Eirunepe', 'America/Eirunepe'), ('Africa/Casablanca', 'Africa/Casablanca'), ('PRC', 'PRC'), ('America/Marigot', 'America/Marigot'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Atka', 'America/Atka'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Halifax', 'America/Halifax'), ('Indian/Mahe', 'Indian/Mahe'), ('Australia/North', 'Australia/North'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Grenada', 'America/Grenada'), ('Africa/Freetown', 'Africa/Freetown'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Madrid', 'Europe/Madrid'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Catamarca', 'America/Catamarca'), ('Africa/Accra', 'Africa/Accra'), ('Asia/Yangon', 'Asia/Yangon'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Denver', 'America/Denver'), ('America/Ojinaga', 'America/Ojinaga'), ('Asia/Aqtau', 'Asia/Aqtau'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Egypt', 'Egypt'), ('Asia/Manila', 'Asia/Manila'), ('Africa/Asmara', 'Africa/Asmara'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Pacific/Johnston', 'Pacific/Johnston'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Santarem', 'America/Santarem'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Cordoba', 'America/Cordoba'), ('HST', 'HST'), ('Africa/Juba', 'Africa/Juba'), ('Africa/Banjul', 'Africa/Banjul'), ('MET', 'MET'), ('America/Guatemala', 'America/Guatemala'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/St_Kitts', 'America/St_Kitts'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Etc/GMT+1', 'Etc/GMT+1'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Asia/Gaza', 'Asia/Gaza'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Africa/Libreville', 'Africa/Libreville'), ('America/Merida', 'America/Merida'), ('Indian/Reunion', 'Indian/Reunion'), ('WET', 'WET'), ('America/Guyana', 'America/Guyana'), ('Asia/Dili', 'Asia/Dili'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Africa/Blantyre', 'Africa/Blantyre'), ('America/Maceio', 'America/Maceio'), ('America/Moncton', 'America/Moncton'), ('America/New_York', 'America/New_York'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Asia/Kuching', 'Asia/Kuching'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/Curacao', 'America/Curacao'), ('Europe/Prague', 'Europe/Prague'), ('Etc/GMT', 'Etc/GMT'), ('Canada/Yukon', 'Canada/Yukon'), ('America/Guayaquil', 'America/Guayaquil'), ('Australia/Queensland', 'Australia/Queensland'), ('Israel', 'Israel'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Nipigon', 'America/Nipigon'), ('Asia/Seoul', 'Asia/Seoul'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Hermosillo', 'America/Hermosillo'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Pacific/Auckland', 'Pacific/Auckland'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Winnipeg', 'America/Winnipeg'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('America/Toronto', 'America/Toronto'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Europe/Paris', 'Europe/Paris'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/St_Lucia', 'America/St_Lucia'), ('Eire', 'Eire'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Kralendijk', 'America/Kralendijk'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Miquelon', 'America/Miquelon'), ('US/Samoa', 'US/Samoa'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Australia/West', 'Australia/West'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Asia/Karachi', 'Asia/Karachi'), ('Etc/GMT-3', 'Etc/GMT-3'), ('US/Alaska', 'US/Alaska'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Europe/Budapest', 'Europe/Budapest'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Europe/Kirov', 'Europe/Kirov'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Macau', 'Asia/Macau'), ('Australia/Hobart', 'Australia/Hobart'), ('Australia/Sydney', 'Australia/Sydney'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Australia/ACT', 'Australia/ACT'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Asia/Kabul', 'Asia/Kabul'), ('Europe/Berlin', 'Europe/Berlin'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Africa/Malabo', 'Africa/Malabo'), ('US/Arizona', 'US/Arizona'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/St_Johns', 'America/St_Johns'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('CET', 'CET'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Yakutat', 'America/Yakutat'), ('Asia/Taipei', 'Asia/Taipei'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Antigua', 'America/Antigua'), ('Europe/Minsk', 'Europe/Minsk'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Mexico/General', 'Mexico/General'), ('Asia/Brunei', 'Asia/Brunei'), ('Etc/GMT-11', 'Etc/GMT-11'), ('UTC', 'UTC'), ('Europe/Busingen', 'Europe/Busingen'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Australia/Perth', 'Australia/Perth'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Malta', 'Europe/Malta'), ('America/Chicago', 'America/Chicago'), ('Canada/Central', 'Canada/Central'), ('Asia/Amman', 'Asia/Amman'), ('America/Louisville', 'America/Louisville'), ('America/Cayman', 'America/Cayman'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Adak', 'America/Adak'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Asia/Vientiane', 'Asia/Vientiane'), ('America/Menominee', 'America/Menominee'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('NZ-CHAT', 'NZ-CHAT'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Australia/Currie', 'Australia/Currie'), ('Pacific/Wake', 'Pacific/Wake'), ('Pacific/Yap', 'Pacific/Yap'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Pacific/Efate', 'Pacific/Efate'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Jujuy', 'America/Jujuy'), ('EET', 'EET'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Pacific/Easter', 'Pacific/Easter'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Africa/Algiers', 'Africa/Algiers'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Europe/Vatican', 'Europe/Vatican'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('America/Dominica', 'America/Dominica'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Africa/Lagos', 'Africa/Lagos'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Chihuahua', 'America/Chihuahua'), ('Australia/Canberra', 'Australia/Canberra'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Swift_Current', 'America/Swift_Current'), ('Zulu', 'Zulu'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Europe/Skopje', 'Europe/Skopje'), ('Universal', 'Universal'), ('Indian/Maldives', 'Indian/Maldives'), ('MST7MDT', 'MST7MDT'), ('Brazil/East', 'Brazil/East'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia')], default='Europe/London', max_length=35),
        ),
    ]
