# Closed boxes

## Problem

Tienes n número de cajas cerradas frente a ti.
Cada caja está numerada secuencialmente de 0 a “n – 1” y cada cuadro puede contener
claves a las otras cajas.
Escriba un método “desbloqueo” que determine si se pueden abrir todas las casillas.

• Prototipo: `def desbloqueo(caja)`

## Input Format

• caja es una lista de listas.

• Una caja es una lista de llaves ejm. [2,8,6] que abren 
otras cajas.

## Constraints

• Puedes asumir que todas las llaves serán enteros positivos.

• Puede haber cajas sin llaves.

• La primera caja “caja[0]” está desbloqueada

## Output Format

• “Return True” Si todas las cajas se pueden abrir, o si no “Return False”

## Samples

### Sample input 0
`[[1], [2], [3], [4], []]`
### Sample output 0
`True`

### Sample input 1
`[[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]`
### Sample output 1
`False`




[Ctrl+K V]

