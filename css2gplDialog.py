
# This file is part of GIMP CSS2GPL Plugin 
# big draft from Gemini logger Pierre Decker
'''
=head1 PARAMETERS

    [PF_FILE,   "file_css", "File CSS ",""],
    [PF_FILE, "file_gpl", "File GPL ", ""],
    [PF_STRING, "name", "Palette name ", ""],
    [PF_SPINNER, "column", "Column number ",1,[1,10,1]],
    [PF_RADIO, "model", "Select model ",0,[Rgb=>0,Hsv=>1]],
    [PF_RADIO, "col", "Order by column ", 0,[RH=>0,GS=>1,BV=>2]],
    [PF_TOGGLE,"order", "Order by ascending ", 1],

'''
class css2gplDialog(GimpUi.ProcedureDialog):
    def __init__(self, procedure):
        super().__init__(procedure=procedure, title="CSS2GPL")
        self.set_border_width(12)

        # Créez une boîte verticale pour organiser les widgets
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.get_content_area().add(vbox)

        # Widget pour le chemin du fichier
        hbox_file = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        label_file = Gtk.Label("Fichier à charger:")
        self.file_entry = Gtk.Entry()
        file_button = Gtk.Button("Parcourir")
        file_button.connect("clicked", self.on_file_button_clicked)
        hbox_file.pack_start(label_file, False, False, 0)
        hbox_file.pack_start(self.file_entry, True, True, 0)
        hbox_file.pack_start(file_button, False, False, 0)
        vbox.pack_start(hbox_file, False, False, 0)

        # Widget pour le nouveau nom
        hbox_nom = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        label_nom = Gtk.Label("Nouveau nom:")
        self.nom_entry = Gtk.Entry()
        hbox_nom.pack_start(label_nom, False, False, 0)
        hbox_nom.pack_start(self.nom_entry, True, True, 0)
        vbox.pack_start(hbox_nom, False, False, 0)
        
        # Widget pour le nombre de colonnes (Spinner)
        hbox_colonnes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        label_colonnes = Gtk.Label("Nombre de colonnes:")
        adjustment = Gtk.Adjustment(value=1, lower=1, upper=10, step_increment=1, page_increment=1)
        self.spin_colonnes = Gtk.SpinButton.new(adjustment, 1, 0)  # 1 pour l'incrément, 0 pour les décimales
        hbox_colonnes.pack_start(label_colonnes, False, False, 0)
        hbox_colonnes.pack_start(self.spin_colonnes, False, False, 0)
        vbox.pack_start(hbox_colonnes, False, False, 0)


        # Widget pour la case à cocher
        self.case_a_cocher = Gtk.CheckButton("Activer une option")
        vbox.pack_start(self.case_a_cocher, False, False, 0)

        self.show_all()

    def on_file_button_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Sélectionner un fichier",
            parent=self,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
        )

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Tous les fichiers")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.file_entry.set_text(dialog.get_filename())

        dialog.destroy()

class css2gplPlugin(Gimp.PlugIn):
    # ... autres méthodes du plugin ...

    def run(self, procedure, image, n_drawables, drawables, args, run_mode):
        if run_mode == Gimp.RunMode.INTERACTIVE:
            dialog = css2gplDialog(procedure)
            response = dialog.run()

            if response == Gtk.ResponseType.OK:
                chemin_fichier = dialog.file_entry.get_text()
                nouveau_nom = dialog.nom_entry.get_text()
                option_activee = dialog.case_a_cocher.get_active()

                # Faites quelque chose avec les valeurs récupérées
                print(f"Fichier à charger: {chemin_fichier}")
                print(f"Nouveau nom: {nouveau_nom}")
                print(f"Option activée: {option_activee}")

                # N'oubliez pas de détruire le dialogue
                dialog.destroy()
                return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())
            else:
                dialog.destroy()
                return procedure.new_return_values(Gimp.PDBStatusType.CANCEL, GLib.Error())
        else:
            # Mode non interactif (pour les scripts)
            return procedure.new_return_values(Gimp.PDBStatusType.NONINTERACTIVE, GLib.Error())

# ... enregistrement du plugin ...
Gimp.main(css2gplPlugin.__gtype__, sys.argv)