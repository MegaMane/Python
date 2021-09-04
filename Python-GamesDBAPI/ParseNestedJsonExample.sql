DECLARE @json NVARCHAR(MAX)=
N'{
    "action":"edit",
    "data": { 
                "2019-08-03":{ 
                                "Description":"sdfsafasdfasdf",
                                "FirstFrozenStep":"333"
                             },
                "2019-08-04":{ 
                                "Description":"blah4",
                                "FirstFrozenStep":"444"
                             }
            }
}';

SELECT A.[action]
      ,B.[key]
      ,C.*
FROM OPENJSON(@json) WITH([action]  NVARCHAR(100)
                         ,[data]    NVARCHAR(MAX) AS JSON) A
OUTER APPLY OPENJSON(A.[data]) B 
OUTER APPLY OPENJSON(B.[value]) WITH([Description] NVARCHAR(100)
                                     ,FirstFrozenStep INT) C;



https://www.nuomiphp.com/eplan/en/652.html