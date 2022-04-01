import csv
import random
from constants import *
from game.casting.animation import Animation
from game.casting.projectils import Projectils
from game.casting.tank import Tank
from game.casting.alien import Alien
from game.casting.bomb import Bombs
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.stats import Stats
from game.casting.text import Text 
from game.casting.bunker import Bunker
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_alien_action import CollideAlienAction
from game.scripting.collide_bombs_action import CollideBombsAction
from game.scripting.collide_tank_action import CollideTankAction
from game.scripting.control_tank_action import ControlTankAction
from game.scripting.control_bomb_action import ControlBombAction
from game.scripting.draw_projectil_action import DrawProjectilAction
from game.scripting.draw_bomb_action import DrawBombAction
from game.scripting.draw_aliens_action import DrawAliensAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_tank_action import DrawTankAction
from game.scripting.draw_bunker_action import DrawBunkerAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_projectil_action import MoveProjectilAction
from game.scripting.move_bomb_action import MoveBombAction
from game.scripting.move_tank_action import MoveTankAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService

class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_ALIENS_ACTION = CollideAlienAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BOMBS_ACTION = CollideBombsAction(PHYSICS_SERVICE, AUDIO_SERVICE, VIDEO_SERVICE)
    COLLIDE_TANK_ACTION = CollideTankAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_TANK_ACTION = ControlTankAction(KEYBOARD_SERVICE)
    CONTROL_BOMB_ACTION = ControlBombAction(KEYBOARD_SERVICE)
    DRAW_TANK_ACTION= DrawTankAction(VIDEO_SERVICE)
    DRAW_BUNKER_ACTION = DrawBunkerAction(VIDEO_SERVICE)
    DRAW_PROJECTIL_ACTION = DrawProjectilAction(VIDEO_SERVICE)
    DRAW_BOMB_ACTION = DrawBombAction(VIDEO_SERVICE)
    DRAW_ALIENS_ACTION = DrawAliensAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_PROJECTIL_ACTION = MoveProjectilAction()
    MOVE_BOMB_ACTION = MoveBombAction()
    MOVE_TANK_ACTION = MoveTankAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass
        
    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_projectils(cast)
        self._add_aliens(cast)
        self._add_tank(cast)
        self._add_bunker(cast)
        self._add_bomb(cast)
        self._add_dialog(cast, ENTER_TO_START)
        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_projectils(cast)
        self._add_aliens(cast)
        self._add_tank(cast)
        self._add_bunker(cast)
        self._add_bomb(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_projectils(cast)
        self._add_aliens(cast)
        self._add_tank(cast)
        self._add_bunker(cast)
        self._add_bomb(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_bomb(cast)
        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_TANK_ACTION)
        script.add_action(INPUT, self.CONTROL_BOMB_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_projectils(cast)
        self._add_tank(cast)
        self._add_bomb(cast)
        self._add_bunker(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_bomb(self, cast):
        #self._keyboard_service = KEYBOARD_SERVICE
        #if self._keyboard_service.is_key_pressed(SPACE):
        for i in range(4):
            bombs = cast.get_actors(BOMBS_GROUP)
            for bomb in bombs:
                bomb.release()

    def _add_aliens(self, cast):
        cast.clear_actors(ALIENS_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    x = FIELD_LEFT + c * ALIENS_WIDTH
                    y = FIELD_TOP + r * ALIENS_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = ALIENS_POINTS 
                    if frames == 1:
                        points *= 2
                    position = Point(x, y)
                    size = Point(ALIENS_WIDTH, ALIENS_HEIGHT)
                    velocity = Point(0, 0)
                    images = ALIENS_IMAGES[color][0:frames]
                    body = Body(position, size, velocity)
                    animation = Animation(images, ALIENS_RATE, ALIENS_DELAY)
                    alien = Alien(body, animation, points)
                    cast.add_actor(ALIENS_GROUP, alien)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_tank(self, cast):
        cast.clear_actors(TANK_GROUP)
        x = CENTER_X - TANK_WIDTH / 2
        y = SCREEN_HEIGHT - TANK_HEIGHT
        position = Point(x, y)
        size = Point(TANK_WIDTH, TANK_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(TANK_IMAGES, TANK_RATE)
        tank = Tank(body, animation)
        cast.add_actor(TANK_GROUP, tank)

    def _add_projectils(self, cast):
        cast.clear_actors(PROJECTILS_GROUP)
        #tank = cast.get_first_actor(TANK_GROUP)
        x = CENTER_X - PROJECTILS_WIDTH / 2
        y = SCREEN_HEIGHT - PROJECTILS_HEIGHT #- TANK_HEIGHT 
        position = Point(x, y)
        size = Point(PROJECTILS_WIDTH, PROJECTILS_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(PROJECTILS_IMAGE)
        projectil = Projectils(body, image, True)
        for i in range(PROJECTILS_NUMBER):
            cast.add_actor(PROJECTILS_GROUP, projectil)

    def _add_bomb(self, cast):
        cast.clear_actors(BOMBS_GROUP)
        for i in range(BOMBS_NUMBER):
            x = random.randint(BOMBS_WIDTH, SCREEN_WIDTH - BOMBS_WIDTH)
            y = FIELD_TOP + 4 * ALIENS_HEIGHT
            position = Point(x, y)
            size = Point(BOMBS_WIDTH, BOMBS_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(BOMBS_IMAGE)
            bomb = Bombs(body, image, True)
        
            cast.add_actor(BOMBS_GROUP, bomb)

    def _add_bunker(self, cast):
        cast.clear_actors(BUNKER_GROUP)
        x = (CENTER_X-300) - BUNKER_WIDTH / 2
        y = SCREEN_HEIGHT - (BUNKER_HEIGHT+100)

        for i in range(3):
            position = Point(x, y)
            size = Point(BUNKER_WIDTH, BUNKER_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            animation = Animation(BUNKER_IMAGES, BUNKER_RATE)
            bunker = Bunker(body, animation)
            x = x + 300
            
            cast.add_actor(BUNKER_GROUP, bunker)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_ALIENS_ACTION)
        script.add_action(OUTPUT, self.DRAW_TANK_ACTION)
        script.add_action(OUTPUT, self.DRAW_BUNKER_ACTION)
        script.add_action(OUTPUT, self.DRAW_PROJECTIL_ACTION)
        script.add_action(OUTPUT, self.DRAW_BOMB_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_PROJECTIL_ACTION)
        script.add_action(UPDATE, self.MOVE_BOMB_ACTION)
        script.add_action(UPDATE, self.MOVE_TANK_ACTION)
        script.add_action(UPDATE, self.COLLIDE_ALIENS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BOMBS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TANK_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)