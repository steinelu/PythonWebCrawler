SELECT D1.DOMAIN, L1.LINK, D2.DOMAIN, L2.LINK FROM REFERENCE
JOIN 
	(SELECT * FROM LINK JOIN DOMAIN ON LINK.DOMAIN = DOMAIN.ID)AS L1
	ON REFERENCE.SRC = L1.ID
JOIN 
	(SELECT * FROM LINK JOIN DOMAIN ON LINK.DOMAIN = DOMAIN.ID) AS L2
	ON REFERENCE.REF = L2.ID
JOIN
	DOMAIN ON L1.DOMAIN = DOMAIN.ID
	AND L2.DOMAIN = DOMAIN.ID;