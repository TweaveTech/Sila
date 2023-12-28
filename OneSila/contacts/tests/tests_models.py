from contacts.models import Company, Supplier, Customer, Influencer, InternalCompany, Person, \
    Address, ShippingAddress, InvoiceAddress
from django.test import TestCase
from core.tests import TestCaseMixin


class CompanyTestCase(TestCaseMixin, TestCase):
    def test_supplier_create(self):
        supplier = Supplier.objects.create(name='test_supplier_create', multi_tenant_company=self.multi_tenant_company)
        self.assertTrue(supplier.is_supplier)

    def test_supplier_qstype(self):
        supplier_id = Supplier.objects.create(name='test_supplier_create', multi_tenant_company=self.multi_tenant_company).id
        supplier = Supplier.objects.get(id=supplier_id)
        all_suppliers = Supplier.objects.all()

        self.assertTrue(all_suppliers, Supplier.objects)
        self.assertTrue(supplier, Supplier)

    def test_supplier_search(self):
        Supplier.objects.create(name='test_search_supplier', multi_tenant_company=self.multi_tenant_company)
        not_me = Supplier.objects.create(name='not_me_test_supplier', multi_tenant_company=self.multi_tenant_company)

        qs = Supplier.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_company_search(self):
        test_search_company = Company.objects.create(name='test_search_company', multi_tenant_company=self.multi_tenant_company)
        not_me = Company.objects.create(name='not_me_test', multi_tenant_company=self.multi_tenant_company)

        qs = Company.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_customer_search(self):
        test_search_company = Customer.objects.create(name='test_search_customer', multi_tenant_company=self.multi_tenant_company)
        not_me = Customer.objects.create(name='not_me_test_customer', multi_tenant_company=self.multi_tenant_company)

        qs = Customer.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_influencer_search(self):
        test_search_company = Influencer.objects.create(name='test_search_Influencer', multi_tenant_company=self.multi_tenant_company)
        not_me = Influencer.objects.create(name='not_me_test_Influencer', multi_tenant_company=self.multi_tenant_company)

        qs = Influencer.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_internalcompany_search(self):
        test_search_company = InternalCompany.objects.create(name='test_search_InternalCompany', multi_tenant_company=self.multi_tenant_company)
        not_me = InternalCompany.objects.create(name='not_me_test_InternalCompany', multi_tenant_company=self.multi_tenant_company)

        qs = InternalCompany.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_person_search(self):
        test_search_company = Person.objects.create(name='test_search_Person', multi_tenant_company=self.multi_tenant_company)
        not_me = Person.objects.create(name='not_me_test_Person', multi_tenant_company=self.multi_tenant_company)

        qs = Person.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_address_search(self):
        test_search_company = Address.objects.create(name='test_search_Address', multi_tenant_company=self.multi_tenant_company)
        not_me = Address.objects.create(name='not_me_test_Address', multi_tenant_company=self.multi_tenant_company)

        qs = Address.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_shippingaddress_search(self):
        test_search_company = ShippingAddress.objects.create(name='test_search_ShippingAddress', multi_tenant_company=self.multi_tenant_company)
        not_me = ShippingAddress.objects.create(name='not_me_test_ShippingAddress', multi_tenant_company=self.multi_tenant_company)

        qs = ShippingAddress.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)

    def test_invoiceaddress_search(self):
        test_search_company = InvoiceAddress.objects.create(name='test_search_InvoiceAddress', multi_tenant_company=self.multi_tenant_company)
        not_me = InvoiceAddress.objects.create(name='not_me_test_InvoiceAddress', multi_tenant_company=self.multi_tenant_company)

        qs = InvoiceAddress.objects.search('search')

        self.assertTrue(qs.exists())
        self.assertTrue(not_me not in qs)
