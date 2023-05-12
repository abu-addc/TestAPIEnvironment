### Diego and Manlika
class InventoryCount:

    def __init__ (self, inventory_id, name, inventory_location, created_by, date_created, list_of_events, counted_by, items_counted, status):
        self.inventory_id = inventory_id
        self.name = name
        self.inventory_location = inventory_location
        self.created_by = created_by
        self.date_created = date_created
        self.list_of_events = list_of_events
        self.counted_by = counted_by
        self.items_counted = items_counted
        self.status = status

    def get_inventory_id(self):
        return self.inventory_id
    
    def set_inventory_id(self, new_inventory_id):
        self.inventory_id = new_inventory_id

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_inventory_location(self):
        return self.inventory_location
    
    def set_inventory_location(self, new_inventory_location):
        self.inventory_location = new_inventory_location

    def get_created_by(self):
        return self.created_by
    
    def set_created_by(self, new_created_by):
        self.created_by = new_created_by

    def get_date_created(self):
        return self.date_created
    
    def set_date_created(self, new_date_created):
        self.date_created = new_date_created

    def get_list_of_events(self):
        return self.list_of_events
    
    def set_list_of_events(self, new_list_of_events):
        self.inventory_id = new_list_of_events

    def get_counted_by(self):
        return self.counted_by
    
    def set_counted_by(self, new_counted_by):
        self.counted_by = new_counted_by
    
    def get_items_counted(self):
        return self.items_counted
    
    def set_items_counted(self, new_items_counted):
        self.items_counted = new_items_counted

    def get_status(self):
        return self.status
    
    def set_status(self, new_status):
        self.status = new_status

    # def toDBCollection(self):
    #     return{
    #         'inventory_id': self.inventory_id,
    #         'name': self.name,
    #         'inventory_location': self.inventory_location,
    #         'created_by': self.created_by,
    #         'date_created': self.date_created,
    #         'list_of_events': self.list_of_events,
    #         'counted_by': self.counted_by,
    #         'items_counted': self.items_counted,
    #         'status': self.status
    #         }