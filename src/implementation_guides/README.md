# Hinweise zu dem Implementation Guides

Die Implementation Guides (IG) geben verbindlich XDS-Metadaten für die Verwendung von strukturierten Dokumenten im Kontext der ePA vor.
Metadaten, die in der IG aufgeführt sind, müssen von Primärsystemen für das Einstellen von strukturierten Dokumenten verwendet werden, nicht aufgeführte Metadaten können unter Berücksichtigung der Vorgaben der Spezifikation gemSpec_DM_ePA, Anforderung A_14760-* "Nutzungsvorgaben für die Verwendung von XDS-Metadaten" frei vergeben werden.

## Versionen der strukturuierten Dokumente
Eine IG definiert die Metadaten, insbesondere den formatCode, immer für eine bestimmte Version eines strukturierten Dokuments. Für neue strukturierte Dokumente oder neue Versionen von strukturierten Dokumenten wird jeweils eine eigene IG neu veröffentlicht.

Eine IG kann sich dabei auf eine ganz spezifische Version beziehen, beispielsweise ig-mothersrecord_V_1_1_0 für das MIO Mutterpass in der Version 1.1.0, und ist auch nur für diese Version anzuwenden. Eine neue Version des MIO, beispielsweise MIO Mutterpass 1.1.1 wird dann durch eine weitere IG (neue Datei) abgedeckt.
IGs können auch für mehrere Patchversionen eines strukturierten Dokuments definiert sein. Beispielsweise ist ig-eau_V_1_1 für alle (KBV-) Versionen zur eAU 1.1.X anzuwenden (Version 1.1.0 bis 1.1.N). Diese Variante wird in der Regel bevorzugt, da die maßgeblichen formatCodes keine Unterscheidung der Patchversion erlauben.


## Gültigkeitszeitraum
Jede IG enthält ein 'validFrom' Datum. Ab diesem Zeitpunkt ist das Einstellen von strukturierten Dokumenten der referenzierten Version mit den vorgebenen Metadaten möglich. Ist der Zeitpunkt noch nicht erreicht, lehnt das ePA-Aktensystem das Einstellen des Dokuments ab.

Jede IG kann ein 'clientReadOnlyFrom' Datum enthalten. Dieses Datum wird dann gesetzt, wenn keine weiteren Dokumente dieser Ausprägung in die ePA eingestellt werden sollen. In der Regel ist dieses der Fall, wenn bereits neue Versionen des strukturierten Dokuments (inklusive einer neuen IG) verfügbar sind. Zuvor eingestellte Dokumente sind weiterhin verfügbar und können gelesen werden, neue Dokumente dieser Ausprägung werden vom ePA-Aktensystem jedoch abgelehnt. 


## Korrekturen der Metadaten
Im Einzefall kann es vorkommen, dass einzelne Metadatenvorgaben in einer IG geändert, bzw. korrigiert, werden müssen. Der geänderte Code wird dann zusätzlich mit in die IG aufgenommen und der zu ersetzende mit einem 'deprecatedFrom' Datum versehen. Der 'deprecated' Code soll ab diesem Datum nicht mehr verwendet werden, Dokumente mit diesem Code werden durch das ePA-Aktensystem aber nicht abgelehnt.

## interne Version einer IG
Bei Änderungen der IG - editorische Anpassungen, geänderte Verweise, Änderung des Gültigkeitszeitraums oder Korrekturen von Metadaten - wird zur Unterscheidung der einzelnen IG Varianten, der Dateiname ändert sich ja nicht, eine interne Versionsnummer mitgeführt ('igVersion') 




