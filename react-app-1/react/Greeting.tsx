import React from 'react'

type Props = {
  name: string
}

function Greeting({ name }: Props) {
  return (
    <div>
      <div>Hey, {name}</div>
      <div>Hey, {name}</div>
    </div>
  )

}

export default Greeting
