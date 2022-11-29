Nslookup fix:

For at forhindre command injection sårbarheden vi så i klassen, har jeg lavet "approved_domains" og "approved_www". 
Derefter et "if" statement der enten udfører commanden eller sender en error.
Dette er gjort for at forhindre at man kan indsætte scripts i inputtet og nu skal inputtet altid skal starte med www. og slutte med enten .dk, .com eller .org.
