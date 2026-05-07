import asyncio
import unittest
from unittest.mock import MagicMock, patch, AsyncMock
from one_soul.profit.main import MasterEntity

class TestMasterEntity(unittest.IsolatedAsyncioTestCase):
    async def test_entity_initialization(self):
        entity = MasterEntity(name="TestSoul")
        self.assertEqual(entity.name, "TestSoul")
        self.assertFalse(entity.is_running)

    async def test_heart_dominant_drive(self):
        entity = MasterEntity()
        entity.heart.profit = 0.9
        entity.heart.love = 0.1
        self.assertEqual(entity.heart.dominant_drive(), "profit")

    @patch('one_soul.profit.memory.scribe.MemoryScribe.ingest_bible', new_callable=AsyncMock)
    @patch('one_soul.profit.muscles.registry.SkillRegistry.load_all', new_callable=MagicMock)
    async def test_awaken_minimal(self, mock_load, mock_ingest):
        entity = MasterEntity()
        # We don't want to run the infinite breathe loop in a test
        async def mock_breathe():
            await asyncio.sleep(0.1)

        with patch.object(entity.kernel, 'breathe', side_effect=mock_breathe):
            await asyncio.wait_for(entity.awaken(), timeout=1.0)
            self.assertTrue(entity.is_running)

    async def test_memory_storage(self):
        entity = MasterEntity()
        await entity.memory.store_memory("Test experience", "episodic", 0.9)
        self.assertEqual(len(entity.memory.episodic_memory), 1)
        self.assertEqual(entity.memory.episodic_memory[0]["content"], "Test experience")

if __name__ == "__main__":
    unittest.main()
