from gym.envs.registration import register

register(
    id='ContinuousCartpole-v0',
    entry_point='gym_continuous_cartpole.envs:ContinuousCartpoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id='ContinuousCartpole-v1',
    entry_point='gym_continuous_cartpole.envs:ContinuousCartpoleEnv',
    max_episode_steps=500,
    reward_threshold=475.0,
)
