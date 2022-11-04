import React from 'react'

type Props = {
  name: string
}

function Greet({ name }: Props) {
  return (
    <div>
      <div>Hey, {name}</div>
      <div>Hey, {name}</div>
      <div>Hey, {name}</div>
      <div>Hey, {name}</div>
    </div>
  )

}

export default Greet
