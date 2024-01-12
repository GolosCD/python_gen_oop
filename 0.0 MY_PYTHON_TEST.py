import re
 
a = '''
 CREATE OR REPLACE FORCE VIEW KHD_PUB.RUFRDM_SBJ_P_V
(SBJ_ID, SBJ_TYPE_CODE, SBJ_KIND_CODE, CERT_SERIES, CERT_CO_CODE, 
 CERT_NUMBER, CERT_NAME, CERT_DATE, END_DATE, ATT_DATE, 
 P_CERT_SERIES, P_CERT_CO_CODE, P_CERT_NUMBER, SYS_DE, SYS_DS, 
 STATUS_VALUE_CODE)
BEQUEATH DEFINER
AS 
select b.sbj_id
			,b.sbj_type_code
      ,'P' as SBJ_KIND_CODE
      ,b.cert_series
      ,b.cert_co_code
      ,b.cert_number
      ,ct.name      as CERT_NAME
      ,b.ds         as CERT_DATE
      ,b.de         as END_DATE
      ,e.start_date as ATT_DATE
      ,lag(b.CERT_SERIES)		over(partition by b.sbj_id,b.exam_id order by b.sbj_id,b.exam_id,b.ds) as P_CERT_SERIES
      ,lag(b.CERT_CO_CODE)	over(partition by b.sbj_id,b.exam_id order by b.sbj_id,b.exam_id,b.ds) as P_CERT_CO_CODE
      ,lag(b.CERT_NUMBER)		over(partition by b.sbj_id,b.exam_id order by b.sbj_id,b.exam_id,b.ds) as P_CERT_NUMBER
      ,to_date('31.12.9999','dd.mm.yyyy') as SYS_DE
      ,current_date as SYS_DS
      ,b.STATUS_VALUE_CODE
from reg_data.CERTIFIED_PERSON_CERT b
	left join reg_data.CERTIFICATION_EXAM e on (b.exam_id=e.id)
--	left join reg_data.CERTIFICATION_TYPE ct on (e.certification_type_code=ct.CODE) -- пришлось исправить из-за грубой ошибки при связывании исторических таблиц
	left join reg_data.certification_type ct on (e.certification_type_code=ct.CODE and b.ds between ct.ds and ct.de);
 '''
 
 
# print(re.findall(r'\bREG_DATA\.\w+\b',a,re.IGNORECASE))


a = a.replace('reg_data.CERTIFICATION_TYPE'.upper(),'reg_data.CERTIFICATION_TYPE_NEW'.upper())

print(a)

print('reg_data.CERTIFICATION_TYPE'.isupper())

print('reg_data.CERTIFICATION_TYPE'.islower())