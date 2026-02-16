John eats
∃e.(Eat(e) ^ Eater(e, John))

a student eats
∃e∃x.(Eat(e) ^ Eater(e, x) ^ Student(x))

all students eat
Ɐx(Student(x) --> ∃e.(Eat(e) ^ Eater(e, x)))

John eats a sandwich
∃e∃x.(Eat(e) ^ Eater(e,John) ^ Sandwich(x) ^ Eaten(e,x))

all students eat or drink
Ɐx(Student(x) --> ∃e.((Eat(e) ^ Eater(e, x)) | (Drink(e) ^ Drinker(e, x))))

John drinks a soda or eats a sandwich
(∃e1∃x.(Drink(e1) ^ Drinker(e1,John) ^ Soda(x) ^ Drunk(e1,x))) | (∃e2∃y.(Eat(e2) ^ Eater(e2,John) ^ Sandwich(y) ^ Eaten(e2,y)))

John or Mary eats
∃e.(Eat(e) ^ (Eater(e, John) | Eater(e, Mary)))

a student writes an essay or eats
∃x.(Student(x) ^ ((∃e1.(Eat(e1) ^ Eater(e1, x))) | (∃e2∃y.(Write(e2) ^ Writer(e2, x) ^ Essay(y) ^ Written(e2, y)))))

every student eats a sandwich or drinks a soda
Ɐx(Student(x) --> (∃e1∃y.(Eat(e1) ^ Eater(e1, x) ^ Sandwich(y) ^ Eaten(e1, y)) | ∃e2∃z.(Drink(e2) ^ Drinker(e2,x) ^ Soda(z) ^ Drank(e2, z))))

John eats every sandwich
Ɐx(Sandwich(x) --> ∃e.(Eat(e) ^ Eater(e, John) ^ Eaten(e, x)))

John eats every sandwich or bagel
Ɐx((Sandwich(x) | Bagel(x)) --> ∃e.(Eat(e) ^ Eater(e, John) ^ Eaten(e, x)))

nobody eats a bagel
¬∃e∃x∃y.(Eat(e) ^ Eater(e, x) ^ Bagel(y) ^ Eaten(e,y))

a person does not eat
∃x.(Person(x) ^ ¬∃e.(Eat(e) ^ Eater(e,x)))

Jack does not eat or drink
¬(∃e1.(Eat(e1) ^ Eater(e1, Jack)) | ∃e2.(Drink(e2) ^ Drinker(e2, Jack)))

no student eats a bagel
Ɐx(Student(x) --> ¬∃e∃y.(Eat(e) ^ Eater(e,x) ^ Bagel(y) ^ Eaten(e, y)))
