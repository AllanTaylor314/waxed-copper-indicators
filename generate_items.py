#!/usr/bin/env python3
"""Generate item definition overrides for all waxed copper variants."""

import json
from pathlib import Path

PACK_ROOT = Path(__file__).parent
ITEMS_DIR = PACK_ROOT / "assets" / "minecraft" / "items"
BADGE_FLAT = {
    "type": "minecraft:model",
    "model": "waxed_copper_indicator:item/honeycomb_badge",
}

BADGE_ISOMETRIC = {
    "type": "minecraft:model",
    "model": "waxed_copper_indicator:item/honeycomb_badge_isometric",
}

# Vanilla base item models for waxed blocks (waxed items reuse unwaxed models).
SIMPLE_MODELS = {
    "waxed_chiseled_copper": "minecraft:block/chiseled_copper",
    "waxed_copper_bars": "minecraft:item/copper_bars",
    "waxed_copper_block": "minecraft:block/copper_block",
    "waxed_copper_bulb": "minecraft:block/copper_bulb",
    "waxed_copper_chain": "minecraft:item/copper_chain",
    "waxed_copper_door": "minecraft:item/copper_door",
    "waxed_copper_golem_statue": None,
    "waxed_copper_grate": "minecraft:block/copper_grate",
    "waxed_copper_lantern": "minecraft:item/copper_lantern",
    "waxed_copper_trapdoor": "minecraft:block/copper_trapdoor_bottom",
    "waxed_cut_copper": "minecraft:block/cut_copper",
    "waxed_cut_copper_slab": "minecraft:block/cut_copper_slab",
    "waxed_cut_copper_stairs": "minecraft:block/cut_copper_stairs",
    "waxed_exposed_chiseled_copper": "minecraft:block/exposed_chiseled_copper",
    "waxed_exposed_copper": "minecraft:block/exposed_copper",
    "waxed_exposed_copper_bars": "minecraft:item/exposed_copper_bars",
    "waxed_exposed_copper_bulb": "minecraft:block/exposed_copper_bulb",
    "waxed_exposed_copper_chain": "minecraft:item/exposed_copper_chain",
    "waxed_exposed_copper_chest": None,
    "waxed_exposed_copper_door": "minecraft:item/exposed_copper_door",
    "waxed_exposed_copper_golem_statue": None,
    "waxed_exposed_copper_grate": "minecraft:block/exposed_copper_grate",
    "waxed_exposed_copper_lantern": "minecraft:item/exposed_copper_lantern",
    "waxed_exposed_copper_trapdoor": "minecraft:block/exposed_copper_trapdoor_bottom",
    "waxed_exposed_cut_copper": "minecraft:block/exposed_cut_copper",
    "waxed_exposed_cut_copper_slab": "minecraft:block/exposed_cut_copper_slab",
    "waxed_exposed_cut_copper_stairs": "minecraft:block/exposed_cut_copper_stairs",
    "waxed_exposed_lightning_rod": "minecraft:block/exposed_lightning_rod",
    "waxed_lightning_rod": "minecraft:block/lightning_rod",
    "waxed_oxidized_chiseled_copper": "minecraft:block/oxidized_chiseled_copper",
    "waxed_oxidized_copper": "minecraft:block/oxidized_copper",
    "waxed_oxidized_copper_bars": "minecraft:item/oxidized_copper_bars",
    "waxed_oxidized_copper_bulb": "minecraft:block/oxidized_copper_bulb",
    "waxed_oxidized_copper_chain": "minecraft:item/oxidized_copper_chain",
    "waxed_oxidized_copper_chest": None,
    "waxed_oxidized_copper_door": "minecraft:item/oxidized_copper_door",
    "waxed_oxidized_copper_golem_statue": None,
    "waxed_oxidized_copper_grate": "minecraft:block/oxidized_copper_grate",
    "waxed_oxidized_copper_lantern": "minecraft:item/oxidized_copper_lantern",
    "waxed_oxidized_copper_trapdoor": "minecraft:block/oxidized_copper_trapdoor_bottom",
    "waxed_oxidized_cut_copper": "minecraft:block/oxidized_cut_copper",
    "waxed_oxidized_cut_copper_slab": "minecraft:block/oxidized_cut_copper_slab",
    "waxed_oxidized_cut_copper_stairs": "minecraft:block/oxidized_cut_copper_stairs",
    "waxed_oxidized_lightning_rod": "minecraft:block/oxidized_lightning_rod",
    "waxed_weathered_chiseled_copper": "minecraft:block/weathered_chiseled_copper",
    "waxed_weathered_copper": "minecraft:block/weathered_copper",
    "waxed_weathered_copper_bars": "minecraft:item/weathered_copper_bars",
    "waxed_weathered_copper_bulb": "minecraft:block/weathered_copper_bulb",
    "waxed_weathered_copper_chain": "minecraft:item/weathered_copper_chain",
    "waxed_weathered_copper_chest": None,
    "waxed_weathered_copper_door": "minecraft:item/weathered_copper_door",
    "waxed_weathered_copper_golem_statue": None,
    "waxed_weathered_copper_grate": "minecraft:block/weathered_copper_grate",
    "waxed_weathered_copper_lantern": "minecraft:item/weathered_copper_lantern",
    "waxed_weathered_copper_trapdoor": "minecraft:block/weathered_copper_trapdoor_bottom",
    "waxed_weathered_cut_copper": "minecraft:block/weathered_cut_copper",
    "waxed_weathered_cut_copper_slab": "minecraft:block/weathered_cut_copper_slab",
    "waxed_weathered_cut_copper_stairs": "minecraft:block/weathered_cut_copper_stairs",
    "waxed_weathered_lightning_rod": "minecraft:block/weathered_lightning_rod",
    "waxed_copper_chest": None,
}

CHEST_MODELS = {
    "waxed_copper_chest": {
        "base": "minecraft:item/copper_chest",
        "texture": "minecraft:copper",
    },
    "waxed_exposed_copper_chest": {
        "base": "minecraft:item/exposed_copper_chest",
        "texture": "minecraft:copper_exposed",
    },
    "waxed_weathered_copper_chest": {
        "base": "minecraft:item/weathered_copper_chest",
        "texture": "minecraft:copper_weathered",
    },
    "waxed_oxidized_copper_chest": {
        "base": "minecraft:item/oxidized_copper_chest",
        "texture": "minecraft:copper_oxidized",
    },
}

GOLEM_TEXTURES = {
    "waxed_copper_golem_statue": "minecraft:textures/entity/copper_golem/copper_golem.png",
    "waxed_exposed_copper_golem_statue": "minecraft:textures/entity/copper_golem/copper_golem_exposed.png",
    "waxed_weathered_copper_golem_statue": "minecraft:textures/entity/copper_golem/copper_golem_weathered.png",
    "waxed_oxidized_copper_golem_statue": "minecraft:textures/entity/copper_golem/copper_golem_oxidized.png",
}


def plain_model(model_id: str) -> dict:
    return {"type": "minecraft:model", "model": model_id}


def chest_model(item_id: str) -> dict:
    info = CHEST_MODELS[item_id]
    return {
        "type": "minecraft:special",
        "base": info["base"],
        "model": {
            "type": "minecraft:chest",
            "texture": info["texture"],
        },
    }


def golem_pose_model(texture: str, pose: str) -> dict:
    return {
        "type": "minecraft:special",
        "base": "minecraft:item/template_copper_golem_statue",
        "model": {
            "type": "minecraft:copper_golem_statue",
            "pose": pose,
            "texture": texture,
        },
    }


def golem_model(item_id: str) -> dict:
    texture = GOLEM_TEXTURES[item_id]
    return {
        "type": "minecraft:select",
        "property": "minecraft:block_state",
        "block_state_property": "copper_golem_pose",
        "cases": [
            {"when": ["sitting"], "model": golem_pose_model(texture, "sitting")},
            {"when": ["running"], "model": golem_pose_model(texture, "running")},
            {"when": ["star"], "model": golem_pose_model(texture, "star")},
        ],
        "fallback": golem_pose_model(texture, "standing"),
        "transformation": {
            "translation": [0.5, 1.5, 0.5],
            "left_rotation": [0, 0, 0, 1],
            "right_rotation": [0, 0, 0, 1],
            "scale": [1, -1, -1],
        },
    }


def base_model_for(item_id: str) -> dict:
    if item_id in CHEST_MODELS:
        return chest_model(item_id)
    if item_id in GOLEM_TEXTURES:
        return golem_model(item_id)
    model_id = SIMPLE_MODELS[item_id]
    if model_id is None:
        raise ValueError(f"No model mapping for {item_id}")
    return plain_model(model_id)


def uses_isometric_badge(base: dict) -> bool:
    """Block-style inventory icons share the isometric display transform."""
    if base.get("type") == "minecraft:model":
        return base.get("model", "").startswith("minecraft:block/")
    if base.get("type") == "minecraft:special":
        return base.get("model", {}).get("type") == "minecraft:chest"
    if base.get("type") == "minecraft:select":
        return base.get("property") == "minecraft:block_state"
    return False


def badge_for(base: dict) -> dict:
    return BADGE_ISOMETRIC if uses_isometric_badge(base) else BADGE_FLAT


def with_gui_badge(base: dict) -> dict:
    return {
        "model": {
            "type": "minecraft:select",
            "property": "minecraft:display_context",
            "cases": [
                {
                    "when": ["gui"],
                    "model": {
                        "type": "minecraft:composite",
                        "models": [base, badge_for(base)],
                    },
                }
            ],
            "fallback": base,
        },
        # "oversized_in_gui": True,
    }


def main() -> None:
    ITEMS_DIR.mkdir(parents=True, exist_ok=True)
    for item_id in sorted(SIMPLE_MODELS):
        output = ITEMS_DIR / f"{item_id}.json"
        output.write_text(json.dumps(with_gui_badge(base_model_for(item_id)), indent=None, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Generated {len(SIMPLE_MODELS)} item definitions in {ITEMS_DIR}")


if __name__ == "__main__":
    main()
