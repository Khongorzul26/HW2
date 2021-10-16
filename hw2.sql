show databases;
use hw;
INSERT INTO `information`
(`id`,
`firstName`,
`lastName`,
`citizenId`,
`age`,
`yearsInCompany`,
`salary`,
`gender`,
`startDate`,
`politicalView`)
VALUES
(20, 'Temuge',	'Erdene',	'BH78',	43,	2,	1.6,	'M',	DATE'2019-02-14','right');

select firstName, lastName from hw.information limit 3;
select firstName, age from information order by age limit 5;

