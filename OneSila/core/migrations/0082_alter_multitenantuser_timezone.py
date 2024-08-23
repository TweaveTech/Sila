# Generated by Django 5.0.2 on 2024-06-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Europe/London', 'Europe/London'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Winnipeg', 'America/Winnipeg'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Santarem', 'America/Santarem'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Chicago', 'America/Chicago'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/Nipigon', 'America/Nipigon'), ('EST5EDT', 'EST5EDT'), ('America/Catamarca', 'America/Catamarca'), ('Africa/Luanda', 'Africa/Luanda'), ('Africa/Malabo', 'Africa/Malabo'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Asia/Dacca', 'Asia/Dacca'), ('UCT', 'UCT'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Inuvik', 'America/Inuvik'), ('Australia/Currie', 'Australia/Currie'), ('America/Caracas', 'America/Caracas'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Iceland', 'Iceland'), ('Africa/Gaborone', 'Africa/Gaborone'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Asia/Omsk', 'Asia/Omsk'), ('Iran', 'Iran'), ('Asia/Brunei', 'Asia/Brunei'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Africa/Freetown', 'Africa/Freetown'), ('Europe/Busingen', 'Europe/Busingen'), ('Pacific/Yap', 'Pacific/Yap'), ('Pacific/Niue', 'Pacific/Niue'), ('Europe/Skopje', 'Europe/Skopje'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Africa/Dakar', 'Africa/Dakar'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Australia/Eucla', 'Australia/Eucla'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Cayenne', 'America/Cayenne'), ('America/Denver', 'America/Denver'), ('PST8PDT', 'PST8PDT'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Brazil/Acre', 'Brazil/Acre'), ('Etc/GMT-13', 'Etc/GMT-13'), ('GMT0', 'GMT0'), ('America/Juneau', 'America/Juneau'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Cayman', 'America/Cayman'), ('Africa/Windhoek', 'Africa/Windhoek'), ('US/East-Indiana', 'US/East-Indiana'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Mexico/General', 'Mexico/General'), ('Africa/Niamey', 'Africa/Niamey'), ('Etc/GMT-3', 'Etc/GMT-3'), ('US/Samoa', 'US/Samoa'), ('Libya', 'Libya'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Pacific/Apia', 'Pacific/Apia'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/Jamaica', 'America/Jamaica'), ('America/Yakutat', 'America/Yakutat'), ('Asia/Harbin', 'Asia/Harbin'), ('Hongkong', 'Hongkong'), ('Asia/Kashgar', 'Asia/Kashgar'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Australia/NSW', 'Australia/NSW'), ('US/Pacific', 'US/Pacific'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Thule', 'America/Thule'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Ojinaga', 'America/Ojinaga'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('CST6CDT', 'CST6CDT'), ('Europe/Berlin', 'Europe/Berlin'), ('US/Eastern', 'US/Eastern'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Grenada', 'America/Grenada'), ('Australia/West', 'Australia/West'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Africa/Libreville', 'Africa/Libreville'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Australia/North', 'Australia/North'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Guyana', 'America/Guyana'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/New_York', 'America/New_York'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Phoenix', 'America/Phoenix'), ('America/Montserrat', 'America/Montserrat'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Pacific/Auckland', 'Pacific/Auckland'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Europe/Kirov', 'Europe/Kirov'), ('Asia/Amman', 'Asia/Amman'), ('Asia/Manila', 'Asia/Manila'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Asia/Dili', 'Asia/Dili'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Europe/Moscow', 'Europe/Moscow'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Etc/GMT-0', 'Etc/GMT-0'), ('America/Toronto', 'America/Toronto'), ('Universal', 'Universal'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/St_Lucia', 'America/St_Lucia'), ('America/La_Paz', 'America/La_Paz'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Iqaluit', 'America/Iqaluit'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/Anguilla', 'America/Anguilla'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Godthab', 'America/Godthab'), ('Brazil/East', 'Brazil/East'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/St_Johns', 'America/St_Johns'), ('build/etc/localtime', 'build/etc/localtime'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Europe/Malta', 'Europe/Malta'), ('America/Sitka', 'America/Sitka'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/Fortaleza', 'America/Fortaleza'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Montreal', 'America/Montreal'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Canada/Yukon', 'Canada/Yukon'), ('Zulu', 'Zulu'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Asia/Beirut', 'Asia/Beirut'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('US/Central', 'US/Central'), ('Egypt', 'Egypt'), ('America/Santiago', 'America/Santiago'), ('Etc/GMT-8', 'Etc/GMT-8'), ('America/St_Vincent', 'America/St_Vincent'), ('Asia/Gaza', 'Asia/Gaza'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Dawson', 'America/Dawson'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Europe/Paris', 'Europe/Paris'), ('America/Panama', 'America/Panama'), ('Europe/Prague', 'Europe/Prague'), ('Indian/Comoro', 'Indian/Comoro'), ('Asia/Seoul', 'Asia/Seoul'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Europe/Bratislava', 'Europe/Bratislava'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Asia/Hovd', 'Asia/Hovd'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Etc/Universal', 'Etc/Universal'), ('America/Monterrey', 'America/Monterrey'), ('America/Aruba', 'America/Aruba'), ('Africa/Kigali', 'Africa/Kigali'), ('Africa/Asmara', 'Africa/Asmara'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/Halifax', 'America/Halifax'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/El_Salvador', 'America/El_Salvador'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Pacific/Kanton', 'Pacific/Kanton'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Europe/Sofia', 'Europe/Sofia'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Curacao', 'America/Curacao'), ('ROC', 'ROC'), ('Europe/Samara', 'Europe/Samara'), ('America/Regina', 'America/Regina'), ('America/Miquelon', 'America/Miquelon'), ('America/Bahia', 'America/Bahia'), ('EET', 'EET'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Louisville', 'America/Louisville'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Noronha', 'America/Noronha'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Australia/Perth', 'Australia/Perth'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Europe/Brussels', 'Europe/Brussels'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Asia/Chita', 'Asia/Chita'), ('America/Jujuy', 'America/Jujuy'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Asuncion', 'America/Asuncion'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Asia/Almaty', 'Asia/Almaty'), ('Pacific/Easter', 'Pacific/Easter'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Factory', 'Factory'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Recife', 'America/Recife'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Mexico_City', 'America/Mexico_City'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Yellowknife', 'America/Yellowknife'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('America/Creston', 'America/Creston'), ('Europe/Monaco', 'Europe/Monaco'), ('America/Boa_Vista', 'America/Boa_Vista'), ('GB-Eire', 'GB-Eire'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Etc/Zulu', 'Etc/Zulu'), ('Etc/UTC', 'Etc/UTC'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Antigua', 'America/Antigua'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Africa/Cairo', 'Africa/Cairo'), ('Europe/Belfast', 'Europe/Belfast'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Indianapolis', 'America/Indianapolis'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Swift_Current', 'America/Swift_Current'), ('Pacific/Palau', 'Pacific/Palau'),
                                   ('CET', 'CET'), ('Australia/ACT', 'Australia/ACT'), ('Europe/Minsk', 'Europe/Minsk'), ('Indian/Maldives', 'Indian/Maldives'), ('Asia/Yangon', 'Asia/Yangon'), ('US/Alaska', 'US/Alaska'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Manaus', 'America/Manaus'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Nome', 'America/Nome'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Australia/Darwin', 'Australia/Darwin'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/Bogota', 'America/Bogota'), ('America/Rainy_River', 'America/Rainy_River'), ('Africa/Lagos', 'Africa/Lagos'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Vancouver', 'America/Vancouver'), ('Etc/UCT', 'Etc/UCT'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Brazil/West', 'Brazil/West'), ('America/Boise', 'America/Boise'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/St_Kitts', 'America/St_Kitts'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Adak', 'America/Adak'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Africa/Juba', 'Africa/Juba'), ('Asia/Khandyga', 'Asia/Khandyga'), ('UTC', 'UTC'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('GMT+0', 'GMT+0'), ('NZ', 'NZ'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Shiprock', 'America/Shiprock'), ('America/Moncton', 'America/Moncton'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Africa/Douala', 'Africa/Douala'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Eirunepe', 'America/Eirunepe'), ('MST7MDT', 'MST7MDT'), ('Indian/Mahe', 'Indian/Mahe'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Chile/Continental', 'Chile/Continental'), ('Europe/Dublin', 'Europe/Dublin'), ('Europe/Rome', 'Europe/Rome'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Australia/Queensland', 'Australia/Queensland'), ('Indian/Cocos', 'Indian/Cocos'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Africa/Harare', 'Africa/Harare'), ('Asia/Saigon', 'Asia/Saigon'), ('GB', 'GB'), ('Asia/Muscat', 'Asia/Muscat'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('MST', 'MST'), ('Jamaica', 'Jamaica'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Asia/Vientiane', 'Asia/Vientiane'), ('America/Havana', 'America/Havana'), ('America/Knox_IN', 'America/Knox_IN'), ('Europe/Podgorica', 'Europe/Podgorica'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Etc/GMT-14', 'Etc/GMT-14'), ('America/Guatemala', 'America/Guatemala'), ('America/Menominee', 'America/Menominee'), ('Africa/Conakry', 'Africa/Conakry'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Kralendijk', 'America/Kralendijk'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Mazatlan', 'America/Mazatlan'), ('America/Cuiaba', 'America/Cuiaba'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Cuba', 'Cuba'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Belize', 'America/Belize'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Asia/Colombo', 'Asia/Colombo'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Tijuana', 'America/Tijuana'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Dominica', 'America/Dominica'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Managua', 'America/Managua'), ('Australia/South', 'Australia/South'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Asia/Damascus', 'Asia/Damascus'), ('Asia/Oral', 'Asia/Oral'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Qatar', 'Asia/Qatar'), ('Asia/Kuching', 'Asia/Kuching'), ('Europe/Athens', 'Europe/Athens'), ('Israel', 'Israel'), ('MET', 'MET'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Africa/Kampala', 'Africa/Kampala'), ('America/Resolute', 'America/Resolute'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Canada/Pacific', 'Canada/Pacific'), ('Kwajalein', 'Kwajalein'), ('Europe/Oslo', 'Europe/Oslo'), ('Australia/Hobart', 'Australia/Hobart'), ('Turkey', 'Turkey'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Merida', 'America/Merida'), ('Indian/Reunion', 'Indian/Reunion'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Macao', 'Asia/Macao'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('US/Michigan', 'US/Michigan'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Navajo', 'Navajo'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Portugal', 'Portugal'), ('W-SU', 'W-SU'), ('Asia/Taipei', 'Asia/Taipei'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Ensenada', 'America/Ensenada'), ('GMT', 'GMT'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Asia/Jayapura', 'Asia/Jayapura'), ('US/Arizona', 'US/Arizona'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Baku', 'Asia/Baku'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Japan', 'Japan'), ('Africa/Bangui', 'Africa/Bangui'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Lima', 'America/Lima'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Aden', 'Asia/Aden'), ('Europe/Saratov', 'Europe/Saratov'), ('America/Barbados', 'America/Barbados'), ('America/Matamoros', 'America/Matamoros'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Eire', 'Eire'), ('Greenwich', 'Greenwich'), ('Pacific/Guam', 'Pacific/Guam'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Australia/LHI', 'Australia/LHI'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Anchorage', 'America/Anchorage'), ('Africa/Accra', 'Africa/Accra'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Rosario', 'America/Rosario'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Shanghai', 'Asia/Shanghai'), ('GMT-0', 'GMT-0'), ('Africa/Bamako', 'Africa/Bamako'), ('US/Mountain', 'US/Mountain'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Africa/Tunis', 'Africa/Tunis'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Tortola', 'America/Tortola'), ('Europe/Kiev', 'Europe/Kiev'), ('NZ-CHAT', 'NZ-CHAT'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('America/Nassau', 'America/Nassau'), ('Africa/Blantyre', 'Africa/Blantyre'), ('America/Detroit', 'America/Detroit'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('America/Cancun', 'America/Cancun'), ('Asia/Aqtau', 'Asia/Aqtau'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Atikokan', 'America/Atikokan'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Europe/Zurich', 'Europe/Zurich'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('PRC', 'PRC'), ('America/Belem', 'America/Belem'), ('Etc/GMT', 'Etc/GMT'), ('WET', 'WET'), ('Europe/Riga', 'Europe/Riga'), ('Africa/Lome', 'Africa/Lome'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Virgin', 'America/Virgin'), ('Asia/Chungking', 'Asia/Chungking'), ('Africa/Bissau', 'Africa/Bissau'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Cordoba', 'America/Cordoba'), ('Europe/Tirane', 'Europe/Tirane'), ('Asia/Hebron', 'Asia/Hebron'), ('HST', 'HST'), ('Pacific/Efate', 'Pacific/Efate'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Europe/Jersey', 'Europe/Jersey'), ('America/Marigot', 'America/Marigot'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Asia/Macau', 'Asia/Macau'), ('Australia/Victoria', 'Australia/Victoria'), ('Singapore', 'Singapore'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Africa/Casablanca', 'Africa/Casablanca'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Australia/Adelaide', 'Australia/Adelaide'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Poland', 'Poland'), ('America/St_Thomas', 'America/St_Thomas'), ('US/Hawaii', 'US/Hawaii'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Europe/Madrid', 'Europe/Madrid'), ('America/Martinique', 'America/Martinique'), ('Asia/Makassar', 'Asia/Makassar'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Etc/GMT0', 'Etc/GMT0'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Asia/Karachi', 'Asia/Karachi'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Atka', 'America/Atka'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Mendoza', 'America/Mendoza'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Maceio', 'America/Maceio'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('America/Montevideo', 'America/Montevideo'), ('US/Aleutian', 'US/Aleutian'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('EST', 'EST'), ('Canada/Central', 'Canada/Central'), ('Africa/Maseru', 'Africa/Maseru'), ('Canada/Eastern', 'Canada/Eastern'), ('Etc/GMT-10', 'Etc/GMT-10'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('ROK', 'ROK')], default='Europe/London', max_length=35),
        ),
    ]
