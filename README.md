# SP_Programowanie_komputerow_lab_GUI
Studia podyplomowe, Programowanie wizualne - Python, Wydział Informatyki, ZUT w Szczecinie - Laboratorium

Zadanie 1. PESEL.
Widżety: 1xLabel, 1xEntry, 1xButton.
Użytkownik wprowadza numer PESEL do widżetu Entry, który powinien uniemożliwiać wprowadzanie znaków innych niż cyfry. 
Po kliknięciu w przycisk „Sprawdź” powinno pojawić się okienko informacyjne potwierdzające poprawność numeru PESEL albo
okienko błędu informujące o zdiagnozowaniu nieprawidłowości. Sprawdzenie powinno być dokładne, a więc obejmować liczbę cyfr, 
poprawność daty urodzenia i dopasowanie cyfry kontrolnej.

Zadanie 2. Kalkulatorek.
Widżety: 2xEntry, 4xRadiobutton, 1xButton.
Użytkownik wprowadza 2 liczby do widżetów Entry, wybiera operację widżetem Radiobutton, a po kliknięciu w przycisk „Oblicz” powinno pojawić się okienko informacyjne, zawierające wynik działania albo okienko błędu wskazujące przyczynę uniemożliwiającą wykonanie żądanej operacji.
Po zamknięciu okna błędu skupienie powinno przenieść się do tego widżetu Entry, w którym wykryto błąd.

Zadanie 3. Żaglowiec.
Widżety: 1xCanvas.
Zadaniem programu jest stworzenie rysunku przedstawiającego żaglowiec. Nie realizujemy żadnej interakcji z użytkownikiem.

Zadanie 4. Musofobia.
Widżety: 1xButton.
Program powinien otworzyć okno o rozmiarze 500x500, w którego lewym górnym rogu pojawia się przycisk z napisem „Złap mnie”. 
Przycisk reaguje na pojawienie się nad nim kursora myszy, przemieszczając się do losowo wybranego miejsca w obrębie okna 
(miejsce to należy dobrać w taki sposób, aby gwarantowało ucieczkę spod kursora).

Zadanie 5. Głowa. Widżety: 1xButton.
Program powinien otworzyć okno o rozmiarze 500x500, w którego środku pojawia się przycisk z bitmapą „questhead”. 
Przycisk reaguje na naciskanie klawiszy kursora (strzałek na klawiaturze), przemieszczając się o jeden piksel w kierunku zadanym klawiszem lub o 5 pikseli, jeżeli użyto klawiszy kursora razem z klawiszem Ctrl. 
Przycisk żadnym swoim fragmentem nie może opuścić obszaru okna. Naciśnięcie klawisza <Esc> kończy pracę programu.

Zadanie 6. Klikacz. Widżety: 25xButton.
Program powinien otworzyć okno, w którym umieszczonych jest 25 widżetów Button (rozmieszczonych w siatce 5x5), 
każdy opatrzony losowo wybraną, unikalną liczbą z przedziału od 1 do 999. 
Zadanie użytkownika polega na klikaniu przycisków w kolejności rosnących liczb. 
Przycisk kliknięty prawidłowostaje się nieaktywny, a pomyślne zakończenie zadania kwitowane jest gratulacjami w okienku informacyjnym.

Zadanie 7. Bitowiec. Widżety: 8xCheckbutton, 1xLabel, 1xButton.
Program prezentuje dziesiętną wartość ośmiobitowej liczby całkowitej. Zakładamy, że checkbutton niezafifkowany reprezentuje bit 0, 
a zafifkowany bit 1. Lewy skrajny checkbutton reprezentuje najstarszy bit.
Wartość powstałej w ten sposób liczby należy pokazać wytłuszczoną czcionką Arial w kolorze niebieskim.
Kliknięcie przycisku „Koniec” powoduje wyjście z programu.

Zadanie 8. OX. Widżety: 9xButton.
Program powinien otworzyć okno, w którym umieszczonych jest 9 „gołych” widżetów Button (rozmieszczonych w siatce 3x3), 
reprezentujących 9 kratek gry w kółko i krzyżyk. Grę rozpoczyna komputer, umieszczając na losowo wybranym przycisku znak 'X'.
Kliknięcie w przycisk, który nie ma jeszcze naniesionego żadnego znaku, oznacza postawienie kółka (znak 'O'). 
W odpowiedzi na ruch użytkownika program odpowiada swoim losowym posunięciem i gra toczy się dalej.
Program powinien wykryć fakt zakończenia gry (wygrana jednej ze stron lub remis) i zakomunikować to okienkiem
informacyjnym. Znaki X i O powinny mieć różne kolory i powinny być naniesione wytłuszczoną czcionką Arial o wielkości 20pt.

