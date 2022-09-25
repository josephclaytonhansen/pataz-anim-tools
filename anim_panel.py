#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

import bpy

# --- PANELS

class PatazAnimToolz (bpy.types.Panel):
	bl_idname = 'OBJECT_PT_PatazAnimToolz'
	bl_label = 'Animation Tools'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'Animation'
	
	@classmethod
	def poll(cls, context):
		return (context.object)
	
	def draw(self, context):
		pass

class PatazAnimToolzOperatorPanel (bpy.types.Panel):
	bl_parent_id = 'OBJECT_PT_PatazAnimToolz'
	bl_idname = 'OBJECT_PT_PatazAnimToolzPanel1'
	bl_label = ''
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'Pataz'
	
	@classmethod
	def poll(cls, context):
		return (context.object)
	
	def draw_header(self, context):
		
		layout = self.layout
		row = layout.row()
		row.label (text = 'Tools', icon = 'TOOL_SETTINGS')
	
	def draw(self, context):
		
		layout = self.layout
		
		box = layout.box()
		box.label(text="Transform Utils")
		row = box.row()
		row.operator("scene.pataz_world_matrix_copy", text="Copy world coords", icon="WORLD")
		row = box.row()
		row.operator("scene.pataz_world_matrix_paste", text="Paste world coords", icon="WORLD")
		row = box.row()
		row.operator("scene.pataz_rel_xform_copy", text="Copy relative coords", icon="GROUP_BONE")
		row = box.row()
		row.operator("scene.pataz_rel_xform_paste", text="Paste relative coords", icon="GROUP_BONE")


class PatazAnimToolzSettingsPanel (bpy.types.Panel):
	bl_parent_id = 'OBJECT_PT_PatazAnimToolz'
	bl_idname = 'OBJECT_PT_PatazAnimSettingzPanel'
	bl_label = ''
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'Animation'
	
	@classmethod
	def poll(cls, context):
		return (context.object)
	
	def draw_header(self, context):
		
		layout = self.layout
		row = layout.row()
		row.label (text = 'Settings', icon = 'SETTINGS')
	
	def draw(self, context):
		
		object = context.object
		scene = context.scene
		tool_settings = context.tool_settings
		
		layout = self.layout
		
		box = layout.box()
		box.label(text="Keying", icon="KEYINGSET")
		row = box.row()
		row.prop(context.tool_settings, "use_keyframe_insert_auto", text="")
		row.prop_search(scene.keying_sets_all, "active", scene, "keying_sets_all", text="")
		row = box.row()
		row.prop(context.preferences.edit, "keyframe_new_interpolation_type", text="")
		row = box.row()
		row.prop(context.preferences.edit, "keyframe_new_handle_type", text="")
		row = box.row()
		row.prop(tool_settings, "keyframe_type", text="")
		row = box.row()
		row.prop(context.preferences.edit, "use_keyframe_insert_needed", text="Only Insert Needed")
		row = box.row()
		row.prop(context.preferences.edit, "use_keyframe_insert_available", text="Only Insert Available")
		row = box.row()
		row.prop(context.tool_settings, "use_keyframe_cycle_aware", text="Cycle Aware Keying")
		
		box = layout.box()
		box.label(text="Playback", icon="PLAY")
		row = box.row()
		row.prop(context.scene, "sync_mode", text="")
		row = box.row()
		if not scene.use_preview_range:
			row.prop(scene, "frame_start", text="Start")
			row.prop(scene, "frame_end", text="End")
		else:
			row.prop(scene, "frame_preview_start", text="Start")
			row.prop(scene, "frame_preview_end", text="End")
		
		box = layout.box()
		box.label(text="Audio", icon="SOUND")
		row = box.row()
		row.prop(context.scene, "use_audio", text="Mute", icon='MUTE_IPO_OFF' if scene.use_audio else 'MUTE_IPO_ON')
		row.prop(context.scene, "use_audio_scrub", text="Scrubbing", icon="SEQ_HISTOGRAM")
		
		box = layout.box()
		box.label(text="Optimisation", icon="ALIASED")
		row = box.row()
		row.prop(context.scene.render, "use_simplify", text="Simplify")
		row.prop(context.scene.render, "simplify_subdivision", text="levels")
		


# --- REGISTER

classes = (
	PatazAnimToolz,
	PatazAnimToolzOperatorPanel,
	PatazAnimToolzSettingsPanel,
)
 
reg_cls, unreg_cls = bpy.utils.register_classes_factory (classes)
 
 
def register():
	reg_cls()
 
def unregister():
	unreg_cls()
 
if __name__ == '__main__':
	register()
