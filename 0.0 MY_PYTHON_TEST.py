# sql_txt = '''SELECT LIC.ID ID,
          # LIC.SBJ_ID SBJ_ID,
          # SBJ.SBJ_TYPE_CODE SBJ_TYPE_CODE,
          # SBJ.SBJ_KIND_CODE SBJ_KIND_CODE,
          # SBJ.INN INN,
          # SBJ.OGRN OGRN,
          # LIC.LIC_TYPE_CODE LIC_TYPE_CODE,
          # LV.LIC_SUBTYPE_CODE LIC_SUBTYPE_CODE,
          # LV.LIC_NUM LIC_NUMBER,
          # LIC.LIC_DATE LIC_DATE,
          # DECODE (LIC.EXPIRE_DATE,
                  # TO_DATE ('31.12.9999', 'DD.MM.YYYY'), NULL,
                  # LIC.EXPIRE_DATE)
             # LIC_EXPIRE,
          # LIC_END.DS LIC_END,
          # SLVB.END_REASON END_REASON,
          # PREV_SBJ_LIC_ID PARENT_ID,
          # R.LIC_DATE PARENT_DATE,
          # LV.STATUS STATUS,
          # LV.DS DS,
          # LV.DE DE,
          # LIC.SYS_DS SYS_DS,
          # TO_DATE ('31.12.9999', 'DD.MM.YYYY') SYS_DE,
          # bd.doc_number,
          # bd.doc_date,
          # LV.AUTO_EXPIRE_DATE
     # FROM reg_data.SBJ_LIC LIC
          # LEFT JOIN KHD_PUB.RUFRDM_SBJ_ch SBJ
             # ON     LIC.SBJ_ID = SBJ.SBJ_ID
                # AND LIC.SBJ_TYPE_CODE = SBJ.SBJ_TYPE_CODE
                # AND SBJ.DE = TO_DATE ('31.12.9999', 'DD.MM.YYYY')
          # LEFT JOIN (    SELECT id ROOT_LIC,
                                # lic_date,
                                # CONNECT_BY_ROOT ID AS LIC_ID
                           # FROM reg_data.SBJ_LIC
                          # WHERE CONNECT_BY_ISLEAF = 1 AND LEVEL <> 1
                     # CONNECT BY PRIOR prev_sbj_lic_id = id) R
             # ON R.LIC_ID = LIC.ID
          # LEFT JOIN reg_data.SBJ_LIC_VER LIC_END
             # ON     LIC.ID = LIC_END.SBJ_LIC_ID
                # AND LIC_END.DE = TO_DATE ('31.12.9999', 'DD.MM.YYYY')
                # AND LIC_END.STATUS IN
                       # ('RESTRICTED',
                        # 'SUSPENDED',
                        # 'ANNULED',
                        # 'CANCELLED',
                        # 'REPLACED')
                # AND LIC_END.DRAFT_ID = 0
          # LEFT JOIN (SELECT DISTINCT
                            # SBJ_LIC_ID,
                            # MIN (OPERATION_BASIS)
                               # KEEP (DENSE_RANK LAST ORDER BY DS)
                               # OVER (PARTITION BY SBJ_LIC_ID)
                               # END_REASON
                       # FROM reg_data.SBJ_LIC_VER_BASIS
                      # WHERE DRAFT_ID = 0) SLVB
             # ON LIC_END.SBJ_LIC_ID = SLVB.SBJ_LIC_ID
          # LEFT JOIN reg_data.SBJ_LIC_VER LV
             # ON LIC.ID = LV.SBJ_LIC_ID AND LV.DRAFT_ID = 0
          # LEFT JOIN (SELECT la.sbj_lic_id ids,
                            # la.main_SBJ_ID sbj_id,
                            # db.doc_number,
                            # db.doc_date,
                            # la.ds
                       # FROM    REG_data.lic_basis_doc la
                            # LEFT JOIN
                               # reg_Data.basis_doc db
                            # ON (la.basis_doc_id = db.id)) bd
             # ON (    lic.id = bd.ids
                 # AND bd.sbj_id = lic.sbj_id
                 # AND bd.ds BETWEEN lv.ds AND lv.de)'''
                 
                 
# table_name = 'KHD_PUB.RUFRDM_LIC_V'


# part_one = 'select * from '


# print(f'{sql_txt}\nminus\n{part_one} {table_name}')

mylist = [1,2,3,4,5,6,7,8,9]

for i in range(5):
    print(mylist[~i])