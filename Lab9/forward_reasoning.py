# Import libraries
import aima.logic
import aima.utils


def get_clauses():
    clauses = list()

    clause = input("New Clause: ")
    # Add first-order logic clauses (rules and fact)
    while clause != "":
        clauses.append(aima.utils.expr(clause))
        clause = input("New Clause: ")

    print()
    return clauses


def tell_kb(kb):
    tell = input("\nTell: ")
    # Add rules and facts with tell
    while tell != "":
        kb.tell(aima.utils.expr(tell))
        tell = input("Tell: ")
    print()


def ask_kb(kb):
    ask = input("\nAsk: ")
    # Ask Knowledge Base
    while ask != "":
        print(list(aima.logic.fol_fc_ask(kb, aima.utils.expr(ask))))
        ask = input("Ask: ")
    print()


def main():
    # Create an array to hold clauses
    clauses = get_clauses()

    # Create a first-order logic knowledge base (KB) with clauses
    kb = aima.logic.FolKB(clauses)

    menu = "0. Exit.\n1. Tell Knowledge Base.\n2. Ask Knowledge Base.\n"

    entry = input(menu)
    while entry != '0':
        if entry == '1':
            tell_kb(kb)
        elif entry == '2':
            ask_kb(kb)
        else:
            print()
        entry = input(menu)


# Tell python to run main method
if __name__ == "__main__":
    # Clause
    # (American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)
    # Enemy(Nono, America)
    # Owns(Nono, M1)
    # Missile(M1)
    # (Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)
    # American(West)
    # Missile(x) ==> Weapon(x)

    # Tell
    # Enemy(Coco, America)
    # Enemy(Jojo, America)
    # Enemy(x, America) ==> Hostile(x)

    # Ask
    # Hostile(x)
    # Criminal(x)
    main()
