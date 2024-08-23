# Generated by Django 5.0.2 on 2024-07-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0120_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Pacific/Noumea', 'Pacific/Noumea'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Canada/Central', 'Canada/Central'), ('Pacific/Saipan', 'Pacific/Saipan'), ('US/Central', 'US/Central'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Asia/Damascus', 'Asia/Damascus'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Lima', 'America/Lima'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Creston', 'America/Creston'), ('Asia/Kabul', 'Asia/Kabul'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Mexico_City', 'America/Mexico_City'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('US/Aleutian', 'US/Aleutian'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Iran', 'Iran'), ('ROK', 'ROK'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Brazil/West', 'Brazil/West'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Etc/GMT-3', 'Etc/GMT-3'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Detroit', 'America/Detroit'), ('Asia/Chita', 'Asia/Chita'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Noronha', 'America/Noronha'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Cuba', 'Cuba'), ('Africa/Kampala', 'Africa/Kampala'), ('America/New_York', 'America/New_York'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Whitehorse', 'America/Whitehorse'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Manaus', 'America/Manaus'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Dominica', 'America/Dominica'), ('America/Matamoros', 'America/Matamoros'), ('MST7MDT', 'MST7MDT'), ('ROC', 'ROC'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Chile/Continental', 'Chile/Continental'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('America/Swift_Current', 'America/Swift_Current'), ('Libya', 'Libya'), ('PST8PDT', 'PST8PDT'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Indian/Comoro', 'Indian/Comoro'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Etc/GMT', 'Etc/GMT'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Pacific/Efate', 'Pacific/Efate'), ('Africa/Libreville', 'Africa/Libreville'), ('Africa/Lagos', 'Africa/Lagos'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Montevideo', 'America/Montevideo'), ('Australia/Perth', 'Australia/Perth'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('EET', 'EET'), ('America/Virgin', 'America/Virgin'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Cayenne', 'America/Cayenne'), ('America/Knox_IN', 'America/Knox_IN'), ('Africa/Accra', 'Africa/Accra'), ('America/Jamaica', 'America/Jamaica'), ('America/Nassau', 'America/Nassau'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Japan', 'Japan'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Asia/Colombo', 'Asia/Colombo'), ('GMT', 'GMT'), ('America/Thule', 'America/Thule'), ('Africa/Harare', 'Africa/Harare'), ('Asia/Hebron', 'Asia/Hebron'), ('Brazil/Acre', 'Brazil/Acre'), ('Europe/Rome', 'Europe/Rome'), ('America/Guyana', 'America/Guyana'), ('America/Chicago', 'America/Chicago'), ('Africa/Lome', 'Africa/Lome'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Kralendijk', 'America/Kralendijk'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Africa/Asmara', 'Africa/Asmara'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Pacific/Easter', 'Pacific/Easter'), ('PRC', 'PRC'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Asia/Oral', 'Asia/Oral'), ('Europe/Kirov', 'Europe/Kirov'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Anguilla', 'America/Anguilla'), ('US/Arizona', 'US/Arizona'), ('Australia/Darwin', 'Australia/Darwin'), ('Etc/GMT+3', 'Etc/GMT+3'), ('America/Iqaluit', 'America/Iqaluit'), ('UCT', 'UCT'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Monterrey', 'America/Monterrey'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Mazatlan', 'America/Mazatlan'), ('Pacific/Palau', 'Pacific/Palau'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Bahia', 'America/Bahia'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Asia/Karachi', 'Asia/Karachi'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Asia/Makassar', 'Asia/Makassar'), ('Africa/Conakry', 'Africa/Conakry'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('US/East-Indiana', 'US/East-Indiana'), ('Europe/Berlin', 'Europe/Berlin'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/St_Thomas', 'America/St_Thomas'), ('MST', 'MST'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Beirut', 'Asia/Beirut'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Europe/Athens', 'Europe/Athens'), ('America/Miquelon', 'America/Miquelon'), ('Eire', 'Eire'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Europe/Vatican', 'Europe/Vatican'), ('GMT0', 'GMT0'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Nome', 'America/Nome'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Pacific/Yap', 'Pacific/Yap'), ('America/Nuuk', 'America/Nuuk'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Aden', 'Asia/Aden'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Zulu', 'Zulu'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/Martinique', 'America/Martinique'), ('America/Belize', 'America/Belize'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('EST5EDT', 'EST5EDT'), ('Asia/Kashgar', 'Asia/Kashgar'), ('America/Menominee', 'America/Menominee'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('America/Curacao', 'America/Curacao'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Ojinaga', 'America/Ojinaga'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Santarem', 'America/Santarem'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Atikokan', 'America/Atikokan'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('US/Mountain', 'US/Mountain'), ('Factory', 'Factory'), ('America/Adak', 'America/Adak'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Africa/Maseru', 'Africa/Maseru'), ('Europe/Riga', 'Europe/Riga'), ('Asia/Baghdad', 'Asia/Baghdad'), ('GMT+0', 'GMT+0'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Cuiaba', 'America/Cuiaba'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Pacific/Truk', 'Pacific/Truk'), ('Asia/Qatar', 'Asia/Qatar'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Phoenix', 'America/Phoenix'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Godthab', 'America/Godthab'), ('Asia/Taipei', 'Asia/Taipei'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Africa/Kigali', 'Africa/Kigali'), ('America/St_Lucia', 'America/St_Lucia'), ('Africa/Tunis', 'Africa/Tunis'), ('Africa/Cairo', 'Africa/Cairo'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Australia/Eucla', 'Australia/Eucla'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Etc/GMT-6', 'Etc/GMT-6'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Yakutat', 'America/Yakutat'), ('America/Nipigon', 'America/Nipigon'), ('Asia/Harbin', 'Asia/Harbin'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Louisville', 'America/Louisville'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Canada/Mountain', 'Canada/Mountain'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Dacca', 'Asia/Dacca'), ('Pacific/Kanton', 'Pacific/Kanton'), ('US/Eastern', 'US/Eastern'), ('America/Rainy_River', 'America/Rainy_River'), ('EST', 'EST'), ('Asia/Almaty', 'Asia/Almaty'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Aruba', 'America/Aruba'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('America/Havana', 'America/Havana'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Dhaka', 'Asia/Dhaka'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Australia/Victoria', 'Australia/Victoria'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('US/Alaska', 'US/Alaska'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Australia/Sydney', 'Australia/Sydney'), ('W-SU', 'W-SU'), ('Indian/Maldives', 'Indian/Maldives'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Asia/Magadan', 'Asia/Magadan'), ('Portugal', 'Portugal'), ('America/Yellowknife', 'America/Yellowknife'), ('Europe/Kiev', 'Europe/Kiev'), ('Canada/Eastern', 'Canada/Eastern'), ('Europe/Sofia', 'Europe/Sofia'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/El_Salvador', 'America/El_Salvador'), ('Asia/Omsk', 'Asia/Omsk'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Brazil/East', 'Brazil/East'), ('Canada/Pacific',
                                   'Canada/Pacific'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Asia/Saigon', 'Asia/Saigon'), ('Jamaica', 'Jamaica'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Europe/Minsk', 'Europe/Minsk'), ('Etc/UCT', 'Etc/UCT'), ('America/Barbados', 'America/Barbados'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Navajo', 'Navajo'), ('America/Boise', 'America/Boise'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Australia/Adelaide', 'Australia/Adelaide'), ('America/Santiago', 'America/Santiago'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Australia/Queensland', 'Australia/Queensland'), ('Asia/Seoul', 'Asia/Seoul'), ('Europe/Madrid', 'Europe/Madrid'), ('US/Pacific', 'US/Pacific'), ('America/Tijuana', 'America/Tijuana'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Europe/Paris', 'Europe/Paris'), ('Pacific/Wallis', 'Pacific/Wallis'), ('WET', 'WET'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Europe/Brussels', 'Europe/Brussels'), ('Pacific/Samoa', 'Pacific/Samoa'), ('CET', 'CET'), ('Europe/Moscow', 'Europe/Moscow'), ('US/Michigan', 'US/Michigan'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('NZ-CHAT', 'NZ-CHAT'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Kwajalein', 'Kwajalein'), ('America/Montserrat', 'America/Montserrat'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Europe/Prague', 'Europe/Prague'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Asia/Hovd', 'Asia/Hovd'), ('Pacific/Wake', 'Pacific/Wake'), ('GB-Eire', 'GB-Eire'), ('Africa/Dakar', 'Africa/Dakar'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Denver', 'America/Denver'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Araguaina', 'America/Araguaina'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Africa/Banjul', 'Africa/Banjul'), ('Indian/Christmas', 'Indian/Christmas'), ('Egypt', 'Egypt'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Kuching', 'Asia/Kuching'), ('America/Belem', 'America/Belem'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Africa/Malabo', 'Africa/Malabo'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Europe/Saratov', 'Europe/Saratov'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Hongkong', 'Hongkong'), ('Europe/Oslo', 'Europe/Oslo'), ('Asia/Amman', 'Asia/Amman'), ('America/Regina', 'America/Regina'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Cordoba', 'America/Cordoba'), ('America/Guatemala', 'America/Guatemala'), ('Africa/Juba', 'Africa/Juba'), ('Australia/Canberra', 'Australia/Canberra'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Etc/GMT-2', 'Etc/GMT-2'), ('US/Samoa', 'US/Samoa'), ('Mexico/General', 'Mexico/General'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Greenwich', 'Greenwich'), ('Iceland', 'Iceland'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Asia/Macao', 'Asia/Macao'), ('Africa/Bamako', 'Africa/Bamako'), ('Europe/Budapest', 'Europe/Budapest'), ('Europe/Monaco', 'Europe/Monaco'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Shiprock', 'America/Shiprock'), ('America/Inuvik', 'America/Inuvik'), ('Europe/London', 'Europe/London'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Indian/Chagos', 'Indian/Chagos'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/St_Vincent', 'America/St_Vincent'), ('America/Mendoza', 'America/Mendoza'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Halifax', 'America/Halifax'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('GB', 'GB'), ('America/Managua', 'America/Managua'), ('Asia/Manila', 'Asia/Manila'), ('Europe/Vienna', 'Europe/Vienna'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Europe/Tirane', 'Europe/Tirane'), ('Europe/Jersey', 'Europe/Jersey'), ('NZ', 'NZ'), ('Australia/NSW', 'Australia/NSW'), ('Asia/Muscat', 'Asia/Muscat'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Dawson', 'America/Dawson'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Europe/Malta', 'Europe/Malta'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Australia/North', 'Australia/North'), ('Africa/Douala', 'Africa/Douala'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Europe/Zurich', 'Europe/Zurich'), ('build/etc/localtime', 'build/etc/localtime'), ('US/Hawaii', 'US/Hawaii'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Yangon', 'Asia/Yangon'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Moncton', 'America/Moncton'), ('America/Toronto', 'America/Toronto'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Africa/Gaborone', 'Africa/Gaborone'), ('America/Rosario', 'America/Rosario'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Dili', 'Asia/Dili'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/St_Kitts', 'America/St_Kitts'), ('America/Jujuy', 'America/Jujuy'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Europe/Busingen', 'Europe/Busingen'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/St_Johns', 'America/St_Johns'), ('America/Panama', 'America/Panama'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Europe/Skopje', 'Europe/Skopje'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Pontianak', 'Asia/Pontianak'), ('CST6CDT', 'CST6CDT'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Recife', 'America/Recife'), ('Universal', 'Universal'), ('Etc/UTC', 'Etc/UTC'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Etc/GMT0', 'Etc/GMT0'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Marigot', 'America/Marigot'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Catamarca', 'America/Catamarca'), ('America/Merida', 'America/Merida'), ('America/Maceio', 'America/Maceio'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Cancun', 'America/Cancun'), ('GMT-0', 'GMT-0'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Europe/Andorra', 'Europe/Andorra'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Atka', 'America/Atka'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Australia/Currie', 'Australia/Currie'), ('HST', 'HST'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Cayman', 'America/Cayman'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Anchorage', 'America/Anchorage'), ('Asia/Gaza', 'Asia/Gaza'), ('Australia/ACT', 'Australia/ACT'), ('America/Caracas', 'America/Caracas'), ('America/Juneau', 'America/Juneau'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Asuncion', 'America/Asuncion'), ('Etc/GMT-14', 'Etc/GMT-14'), ('America/Vancouver', 'America/Vancouver'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Resolute', 'America/Resolute'), ('America/Montreal', 'America/Montreal'), ('Africa/Freetown', 'Africa/Freetown'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Ensenada', 'America/Ensenada'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Baku', 'Asia/Baku'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Europe/Samara', 'Europe/Samara'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('MET', 'MET'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Australia/LHI', 'Australia/LHI'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Canada/Yukon', 'Canada/Yukon'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Macau', 'Asia/Macau'), ('Turkey', 'Turkey'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Singapore', 'Singapore'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Poland', 'Poland'), ('Africa/Niamey', 'Africa/Niamey'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Antigua', 'America/Antigua'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/Chihuahua', 'America/Chihuahua'), ('UTC', 'UTC'), ('America/Grenada', 'America/Grenada'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Dubai', 'Asia/Dubai'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Australia/West', 'Australia/West'), ('Israel', 'Israel'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Africa/Algiers', 'Africa/Algiers'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Africa/Bissau', 'Africa/Bissau'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Bogota', 'America/Bogota'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Asia/Brunei', 'Asia/Brunei'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Sitka', 'America/Sitka'), ('Australia/Hobart', 'Australia/Hobart'), ('America/Tortola', 'America/Tortola'), ('Indian/Mahe', 'Indian/Mahe'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Australia/South', 'Australia/South'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Asia/Tehran', 'Asia/Tehran'), ('America/La_Paz', 'America/La_Paz'), ('Etc/Zulu', 'Etc/Zulu')], default='Europe/London', max_length=35),
        ),
    ]
