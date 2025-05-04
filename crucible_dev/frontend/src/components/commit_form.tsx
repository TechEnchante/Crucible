import { useState } from 'react';
import { createCommit } from '../lib/api';
import { Button, Input, Textarea } from 'shadcn/ui';

export function CommitForm({ userId }: { userId: string }) {
  const [message, setMessage] = useState('');

  async function handleSubmit() {
    await createCommit(userId, message);
    setMessage('');
  }

  return (
    <div>
      <Textarea
        placeholder="What did you accomplish today?"
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <Button onClick={handleSubmit}>Commit</Button>
    </div>
  );
}