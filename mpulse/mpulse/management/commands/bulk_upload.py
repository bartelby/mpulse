import csv
from ._bulk_manager import BulkCreateManager
from mpulseapi.models import Member
from django.core.management.base import BaseCommand, CommandError

##############
# Bulk Upload code borrowed from https://www.caktusgroup.com/blog/2019/01/09/django-bulk-inserts/
##############

class Command(BaseCommand):
    help = "Performs bulk uploads from csf file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file_name", type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_name']
        with open(csv_file_path, 'r') as csv_file:
            bulk_mgr = BulkCreateManager(chunk_size=100)
            first_line = True
            for row in csv.reader(csv_file):
                if first_line:
                    first_line = False
                else:
                    print(row)
                    bulk_mgr.add(Member( 
                                        first_name=row[1], 
                                        last_name=row[2],
                                        phone_number=row[3],
                                        client_member_id=row[4],
                                        account_id=row[5]
                                        ))
        bulk_mgr.done()



