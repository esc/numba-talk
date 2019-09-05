from string import Template


t = Template("""==== Example ====

* Sieve of Erastothenes

<[center]
    <<<images/sieve-$i.png, scale=0.50>>>
[center]>
""")
for i in range(159):
    print(t.substitute(i=i))
