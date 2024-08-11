class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Определяет базу данных, которая будет использоваться для операций чтения"""
        if model._meta.app_label == 'one':
            return 'os1'
        elif model._meta.app_label == 'two':
            return 'os2'
        return None

    def db_for_write(self, model, **hints):
        """Определяет базу данных, используемую для операций записи"""
        if model._meta.app_label == 'one':
            return 'os1'
        elif model._meta.app_label == 'two':
            return 'os2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Определяет, разрешены ли отношения между объектами"""
        if obj1._state.db == 'os1' and obj2._state.db == 'os1':
            return True
        if obj1._state.db == 'os2' and obj2._state.db == 'os2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Determines if a model should be migrated in a specific database"""
        if app_label == 'one':
            return db == 'os1'
        elif app_label == 'two':
            return db == 'os2'
        return None
