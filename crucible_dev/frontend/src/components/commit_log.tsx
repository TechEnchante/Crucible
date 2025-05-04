import { useEffect, useState } from 'react';

export function CommitLog() {
  const [commits, setCommits] = useState<any[]>([]);

  useEffect(() => {
    async function fetchCommits() {
      const res = await fetch('/api/commits');
      setCommits(await res.json());
    }
    fetchCommits();
  }, []);

  return (
    <ul>
      {commits.map(c => (
        <li key={c.timestamp}>{new Date(c.timestamp).toLocaleString()} – {c.message}</li>
      ))}
    </ul>
  );
}