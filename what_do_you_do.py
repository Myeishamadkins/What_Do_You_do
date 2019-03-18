def main():

    # if name == 'Glen Evens' or name == 'Kagan Coughlin':
    #     print('Co-Founder')
    # elif name == 'Bethany Copper' or name == 'Sage Nichols' or name == 'John Marsalis':
    #     print('Founding Trustee')
    # elif name == 'Caral Lewis':
    #     print('Trustee')
    # elif name == 'Sean Anthony':
    #     print('Director')
    # elif name == 'Nate Clark':
    #     print('Technical Director')
    # elif name == 'Cole Anderson' or name == 'Timothy Bowling' or name == 'Logan Harrell' or name == 'Desma Hervey' or name == 'Ginger Keys' or name == 'Matt Lipsey' or name == 'Myeisha Madkins' or name == 'Henry Moore' or name == 'John Morgan' or name == 'Irma Patton' or name == 'Danny Peterson' or name == 'Jakylan Standifer' or name == 'Justice Taylor' or name == 'Ray Turner' or name == 'Cody van der Poel' or name == 'Andrew Wheeler':
    #     print('Current Student')
    # elif name == 'Alexandra Fortner' or name == 'Edgar Guzman' or name == "Jo'Tavious Smith" or name == 'Jose Vargas' or name == 'Lizeth Buenrostro' or name == 'Maegan Avant' or name == 'Osvaldo Quinonez' or name == 'Sara Hester' or name == 'Shedlia Freeman' or name == 'Trey Shelton' or name == 'Valente Alvarez' or name == 'Angel Zapata':
    #     print('Graduated 2018')
    # elif name == 'Adam Tutor' or name == 'Addey Welch' or name == 'Dustin Buice' or name == 'Eddrick Butler' or name == 'Jacob Spence' or name == 'James Hakim' or name == 'James Sibert' or name == 'Keegan Faustin' or name == 'Martin Guzman' or name == 'Milttreonna Owens' or name == 'Nicole Shelton' or name == 'Ricky Keisling':
    #     print('Graduated 2017')
    # else:
    #     print('This is not a member of Base Camp. ')

    person = {
        'Co-Founder': {'Glen Evens', 'Kagan Coughlin'},
        'Founding Trustee':
        {'Bethany Cooper', 'Sage Nichols', 'John Marsalis'},
        'Trustee': {'Caral Lawis'},
        'Director': {'Sean Anthony'},
        'Technical Director': {'Nate Clark'},
        'Current Student': {
            'Cole Anderson', 'Timothy Bowling', 'Logan Harrell',
            'Desma Hervey', 'Ginger Keys', 'Matt Lipsey', 'Myeisha Madkins',
            'Henry Moore', 'John Morgan', 'Irma Patton', 'Danny Peterson',
            'Jakylan Standifer', 'Justice Taylor', 'Ray Turner',
            'Cody van der Poel', 'Andrew Wheeler'
        },
        'Graduated 2018': {
            'Alexandra Fortner', 'Edgar Guzman', "Jo'Tavious Smith",
            'Jose Vargas', 'Lizeth Buenrostro', 'Maegan Avant',
            'Osvaldo Quinonez', 'Sara Hester', 'Shedlia Freeman',
            'Trey Shelton', 'Valente Alvarez', 'Angel Zapata'
        },
        'Graduated 2017': {
            'Adam Tutor', 'Addey Welch', 'Dustin Buice', 'Eddrick Butler',
            'Jacob Spence', 'James Hakim', 'James Sibert', 'Keegan Faustin',
            'Martin Guzman', 'Milttreonna Owens', 'Nicole Shelton',
            'Ricky Keisling'
        }
    }

    name = input("Name: ")
    for job, people in person.items():
        if name in people:
            print(job)


if __name__ == '__main__':
    main()
