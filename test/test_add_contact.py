from python_training.model.contact import Contact


def test_add_contact(app):
    app.contact.open_contact_page()
    app.contact.add_new_contact(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", company="1", address="1", home="1", mobile="1", work="1", fax="1", email="test@mail.ru", homepage="mail.ru", Year="1989", address2="next one", phone2="home", notes="Last test"))
