# gallring

Skript för att radera beståndsposter och kurslitteraturmärkningar: 
- getHold tar emot en lista med Libris-id:n och returnerar en lista över samtliga beståndsposter vi har knutna till dessa.
- deletePost tar emot en lista med beståndsposter och raderar dessa.
- removeRefs tar emot en lista med beståndsposter och tar bort deras kurslitteraturmärkning om sådan finns.
- fonster fungerar som grafiskt gränssnitt och tar emot den textfil, innehållande Libris-id:n, vi vill använda oss av. Därefter körs antingen deletePost eller removeRefs.

