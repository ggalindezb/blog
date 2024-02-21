import './Header.css'

export default function Header() {
  return (
    <header>
      <div className="logo">
        <img src="/logo.png" alt="log" />
      </div>
      <div className="navigation">
        <nav>
          <ul>
            <li>Posts</li>
            <li>TIL</li>
            <li>Snips</li>
          </ul>
        </nav>
      </div>
    </header>
  )
}
